from __future__ import annotations

import json
import logging
import platform
import sys

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import joblib 
import numpy as np
import pandas as pd

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import KFold, cross_validate, train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score


@dataclass(frozen=True)
class Config:

    random_state: int = 42

    test_size: float = 0.30
    cv_folds: int   = 5

    BASE_DIR = Path(__file__).resolve().parent
    # artifact_dir: Path = Path("artifacts")
    artifact_dir: Path = BASE_DIR / "artifacts"
    model_filename: str = "regression_model.joblib"
    metadata_filename: str = "metadata.json"

    target_column: str  = "tip_amount"
    
    numeric_features: tuple [str, ...] = (
        "VendorID",
        "passenger_count",
        "trip_distance",
        "RatecodeID",
        "PULocationID",
        "DOLocationID",
        "payment_type",
        "fare_amount",
        "mta_tax",
        "tolls_amount",
        "improvement_surcharge",
    )

CONFIG = Config()


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)

logger = logging.getLogger("ml_regression_training")


def dataset_analysis(
    data: pd.DataFrame,
    target_column: str,
) -> dict[str, Any]:
    """
    Perform exploratory analysis and calculate target correlations.
    """

    logger.info("Performing dataset analysis....")
    numeric_data    =   data.select_dtypes(include=[np.number])

    try:
        if target_column in numeric_data.columns:
            correlations = (
                numeric_data.corr()[target_column]
                .drop(target_column)
                .to_dict()
            )
        else: 
            correlations = {}
        
        summary = {
            "num_rows"      : len(data),
            "num_columns"   : len(data.columns),
            "target_mean"   : float(data[target_column].mean()),
            "target_std"    : float(data[target_column].std()),
            "correlations"  : correlations
        }

        logger.info(
            "Dataset loaded. Rows: %d, Columns:%d",
            summary["num_rows"],
            summary["num_columns"]
        )
        return summary
    except Exception as e:
        raise ValueError("failed to dataset analysis %s",e)

def validate_dataset(
    data: pd.DataFrame,
    config: Config,
) -> None:
    """
    Validate dataset structure, required columns, and basic integrity.
    """

    required_columns = set (
        config.numeric_features +
        (config.target_column,)
    )

    missing_columns = required_columns - set(data.columns)

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {sorted(missing_columns)}"
        )
    if data.empty:
        raise ValueError("Dataset is empty.")

    if data[config.target_column].isna().any():
        raise ValueError("Target column contains missing values.")

    logger.info(
        "Dataset validation passed: rows=%d columns=%d",
        len(data),
        len(data.columns),
    )

def build_preprocessor(
    config: Config,
) -> ColumnTransformer:
    """
    Construct leak-free preprocessing pipelines for numeric and categorical features.
    """
    try:
        transformers=[]
        if config.numeric_features:
            numeric_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="median")),
                    ("scalar", StandardScaler()),
                ]
            )
            transformers.append(
                ("numeric", numeric_pipeline, list(config.numeric_features))
            )
            logger.info("preprocessing completed")
        return ColumnTransformer(
            transformers=transformers,
            remainder="drop"
        )   
    except Exception as e:
        raise ValueError("Preprocessing failed %s", e)

def build_model(config: Config) -> DecisionTreeRegressor:
    """
    Instantiate DecisionTreeRegressor model with target parameters.
    """
    return DecisionTreeRegressor(
        criterion="squared_error",
        max_depth=8,
        random_state=config.random_state,
    )

def build_pipeline(config: Config) -> Pipeline:
    """
    Combine preprocessing and model into a single serializable object.
    """
    return Pipeline(
        steps=[
            ("preprocessor", build_preprocessor(config)),
            ("model", build_model(config)),
        ]
    )

def split_dataset(
    data: pd.DataFrame,
    config: Config,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """
    Split data into training and evaluation sets.
    """
    features = list(config.numeric_features)
    X = data[features]
    y = data[config.target_column]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=config.test_size,
        random_state=config.random_state,
    )

    logger.info(
        "Train rows=%d | Test rows=%d",
        len(X_train),
        len(X_test),
    )

    return X_train, X_test, y_train, y_test

def evaluate_regressor(
    model: Pipeline,
    X_test: pd.DataFrame,
    y_test: pd.Series,
) -> dict[str, float]:
    """
    Evaluate regression metrics (MSE, RMSE, R²).
    """

    predictions = model.predict(X_test)
    mse = float(mean_squared_error(y_test, predictions))

    return {
        "mse": mse,
        "rmse": float(np.sqrt(mse)),
        "r2": float(r2_score(y_test, predictions)),
    }

def cross_validate_regressor(
    model: Pipeline,
    X_train: pd.DataFrame,
    y_train: pd.Series,
    config: Config,
) -> dict[str, float]:
    """
    Perform K-fold cross-validation on regression model.
    """

    cv = KFold(
        n_splits=config.cv_folds,
        shuffle=True,
        random_state=config.random_state,
    )

    scoring = {
        "neg_mean_squared_error": "neg_mean_squared_error",
        "r2": "r2",
    }
    results = cross_validate(
        model,
        X_train,
        y_train,
        cv=cv,
        scoring=scoring,
        n_jobs=-1,
        return_train_score=False,
    )

    cv_metrics = {
        "mse_mean": float(-np.mean(results["test_neg_mean_squared_error"])),
        "mse_std": float(np.std(results["test_neg_mean_squared_error"])),
        "r2_mean": float(np.mean(results["test_r2"])),
        "r2_std": float(np.std(results["test_r2"])),
    }

    return cv_metrics


def build_metadata(
    config: Config,
    metrics: dict[str, float],
    dataset: pd.DataFrame,
) -> dict[str, Any]:
    """
    Build executon metadata for model tracking and reproducibility.
    """

    return{
        "created_at": datetime.now(timezone.utc).isoformat(),
        "target": config.target_column,
        "features": {
            "numeric": list(config.numeric_features),
        },
        "dataset":{
            "rows": int(len(dataset)),
            "columns": int(len(dataset.columns))
        },
        "model": {
            "algorithm" : "DecisionTreeRegressior",
            "max_depth": 8,
            "criterion" : "squared_error",
        },
        "metrics":metrics,
        "enviroment": {
            "python" : sys.version,
            "platform": platform.platform(),
            "numpy" : np.__version__,
            "pandas" : pd.__version__,
        },
    }

def save_artifacts(
    model: Pipeline,
    metadata: dict[str, Any],
    config: Config,
) -> None:
    """
    Persist model binary and metadata cleanly
    """
    config.artifact_dir.mkdir(parents=True, exist_ok=True)

    model_path = config.artifact_dir / config.model_filename
    metadata_path = config.artifact_dir / config.metadata_filename 

    joblib.dump(model, model_path, compress=3)

    with metadata_path.open("w", encoding="utf-8") as file:
        json.dump(metadata, file, indent=2)
    
    logger.info("Model saved to %s", model_path)
    logger.info("Metadata saved to %s", metadata_path)

def train(
    data: pd.DataFrame,
    config: Config,
) -> tuple[Pipeline, dit[str, float]]:
    """
    Full pipeline execution entry point.
    """

    # 1. Dataset Analysis & Validation
    analysis_results = dataset_analysis(data, Config.target_column)
    validate_dataset(data, config)

    # 2. Train/Test Split
    X_train, X_test, y_train, y_test = split_dataset(data, config)

    # 3. Build Pipeline
    model_pipeline = build_pipeline(config)
    
    # 4. Cross-Validation
    logger.info("Running %d-fold cross-validation...", config.cv_folds)
    cv_metrics = cross_validate_regressor(model_pipeline, X_train, y_train, config)
    logger.info("CV MSE: %.4f +/- %.4f", cv_metrics["mse_mean"], cv_metrics["mse_std"])
    logger.info("CV R^2: %.4f +/- %.4f", cv_metrics["r2_mean"], cv_metrics["r2_std"])

    # 5. Final Model Training
    logger.info("Training final Decision Tree Regressor model....")
    model_pipeline.fit(X_train, y_train)

    # 6. Test Set Evaluation
    test_metrics = evaluate_regressor(model_pipeline,X_test, y_test)
    logger.info(
        "Test Set Evaluation | MSE: %.4f | RMSE: %.4f | R^2: %.4f",
        test_metrics["mse"],
        test_metrics["rmse"],
        test_metrics["r2"],
    )

    all_metrics = {
        **cv_metrics,
        **{f"test_{key}": val for key, val in test_metrics.items()},
    }

    # 7. Save Artifacts
    metadata = build_metadata(config, all_metrics, data)
    save_artifacts(model_pipeline, metadata, config)

    return model_pipeline, all_metrics 



def main() -> None:
    url = (
        "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/"
        "pu9kbeSaAtRZ7RxdJKX9_A/yellow-tripdata.csv"
    )

    logger.info("Loading yellow tripdata dataset....")
    data = pd.read_csv(url)
    data.columns = data.columns.str.strip()

    train(data=data, config=CONFIG)

if __name__ == "__main__":
    main()