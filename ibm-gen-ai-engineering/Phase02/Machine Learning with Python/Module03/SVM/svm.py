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
import sklearn

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)
from sklearn.model_selection import (
    StratifiedKFold,
    cross_validate,
    train_test_split,
)
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC

# ============================================================
# CONFIGURATION
# ============================================================

@dataclass(frozen=True)
class Config:
    random_state: int = 42
    test_size: float = 0.30
    cv_folds: int = 5

    BASE_DIR = Path(__file__).resolve().parent
    artifact_dir: Path = BASE_DIR / "artifacts"
    model_filename: str = "svm_model.joblib"
    metadata_filename: str = "metadata.json"

    target_column: str = "Class"
    
    numeric_features: tuple[str, ...] = (
        "V1", "V2", "V3", "V4", "V5", "V6", "V7", "V8", "V9", "V10",
        "V11", "V12", "V13", "V14", "V15", "V16", "V17", "V18", "V19", "V20",
        "V21", "V22", "V23", "V24", "V25", "V26", "V27", "V28", "Amount"
    )

CONFIG = Config()

# ============================================================
# LOGGING
# ============================================================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)

logger = logging.getLogger("svm_training")

# ============================================================
# DATA VALIDATION
# ============================================================

def validate_dataset(
    data: pd.DataFrame,
    config: Config,
) -> None:
    """
    Validate the minimum schema, required columns, missing values, and target class balance.
    """
    if data.empty:
        raise ValueError("Dataset is empty.")

    required_columns = set(config.numeric_features) | {config.target_column}
    missing_columns = required_columns - set(data.columns)

    if missing_columns:
        raise ValueError(
            f"Missing required columns in dataset: {sorted(missing_columns)}"
        )

    if data[config.target_column].isna().any():
        raise ValueError(f"Target column '{config.target_column}' contains NaN values.")

    unique_classes = data[config.target_column].nunique()
    if unique_classes < 2:
        raise ValueError(
            f"Target column '{config.target_column}' must contain at least two unique classes, "
            f"found {unique_classes}."
        )

    feature_nans = data[list(config.numeric_features)].isna().sum().sum()
    if feature_nans > 0:
        logger.warning(
            "Found %d missing values across feature columns. Ensure pipeline imputation handles this.",
            feature_nans
        )

    logger.info(
        "Dataset validation passed: rows=%d, columns=%d",
        len(data),
        len(data.columns)
    )

# ============================================================
# PREPROCESSOR
# ============================================================

def build_preprocessor(
    config: Config,
) -> ColumnTransformer:
    """
    Build preprocessing that can safely be fitted inside 
    a model Pipeline to prevent train/test preprocessing leakage. 
    """
    numeric_pipeline = Pipeline(
        steps=[
            (
                "imputer",
                SimpleImputer(strategy="median")
            ),
            (
                "scaler",
                StandardScaler(),
            ),
        ]
    )

    return ColumnTransformer(
        transformers=[
            (
                "numeric",
                numeric_pipeline,
                list(config.numeric_features)
            )
        ],
        remainder="drop"
    )

# ============================================================
# MODEL
# ============================================================

def build_model(config: Config) -> LinearSVC:
    """
    Instantiate SVM model solving primal optimization (dual=False)
    for fast convergence on large sample sizes (N >> D).
    """
    return LinearSVC(
        class_weight="balanced",
        C=0.005,
        random_state=config.random_state,
        loss="squared_hinge",
        fit_intercept=True,
        dual=False,  # Solves primal optimization problem; fixes ConvergenceWarning for N >> D
        max_iter=10000,
        tol=1e-4,
    )

# ============================================================
# COMPLETE ML PIPELINE
# ============================================================

def build_pipeline(config: Config) -> Pipeline:
    """
    Combine preprocessing + model into one serializable object.
    """
    return Pipeline(
        steps=[
            (
                "preprocessor",
                build_preprocessor(config),
            ),
            (
                "model",
                build_model(config),
            ),
        ]
    )

# ============================================================
# SPLIT DATASET
# ============================================================

def split_dataset(
    data: pd.DataFrame,
    config: Config,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """
    Split data into training and testing sets with target stratification.
    """
    features = list(config.numeric_features)
    X = data[features]
    y = data[config.target_column]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=config.test_size,
        random_state=config.random_state,
        stratify=y,  
    )

    logger.info(
        "Train rows = %d | Test rows = %d",
        len(X_train),
        len(X_test)
    )

    return X_train, X_test, y_train, y_test

# ============================================================
# METRICS
# ============================================================

def evaluate_classifier(
    model: Pipeline,
    X_test: pd.DataFrame,
    y_test: pd.Series | np.ndarray,
) -> dict[str, float]:
    """
    Evaluate a binary classifier.
    """
    predictions = model.predict(X_test)

    metrics = {
        "accuracy": float(
            accuracy_score(y_test, predictions)
        ),
        "precision": float(
            precision_score(
                y_test,
                predictions,
                zero_division=0,
            )
        ),
        "recall": float(
            recall_score(
                y_test,
                predictions,
                zero_division=0,
            )
        ),
        "f1": float(
            f1_score(
                y_test,
                predictions,
                zero_division=0,
            )
        ),
    }

    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba(X_test)[:, 1]
        metrics["roc_auc"] = float(
            roc_auc_score(y_test, probabilities)
        )
    elif hasattr(model, "decision_function"):
        scores = model.decision_function(X_test)
        metrics["roc_auc"] = float(
            roc_auc_score(y_test, scores)
        )
    else:
        logger.warning("Model lacks decision_function and predict_proba; ROC-AUC skipped.")
        
    return metrics

# ============================================================
# CROSS VALIDATION
# ============================================================

def cross_validate_model(
    model: Pipeline,
    X_train: pd.DataFrame,
    y_train: pd.Series | np.ndarray,
    config: Config,
) -> dict[str, float]:
    """
    Perform stratified K-fold cross-validation.
    """
    cv = StratifiedKFold(
        n_splits=config.cv_folds,
        shuffle=True,
        random_state=config.random_state,
    )

    scoring = {
        "accuracy": "accuracy",
        "precision": "precision",
        "recall": "recall",
        "f1": "f1",
        "roc_auc": "roc_auc",
    }

    results = cross_validate(
        model,
        X_train,
        y_train,
        cv=cv,
        scoring=scoring,
        n_jobs=-1,
        return_train_score=False
    )

    cv_metrics = {}

    for metric in scoring:
        values = results[f"test_{metric}"]
        cv_metrics[f"{metric}_mean"] = float(np.mean(values))
        cv_metrics[f"{metric}_std"] = float(np.std(values))
        
    return cv_metrics

# ============================================================
# METADATA
# ============================================================

def build_metadata(
    config: Config,
    metrics: dict[str, float],
    dataset: pd.DataFrame,
) -> dict[str, Any]:
    """
    Build a comprehensive metadata dictionary tracking run details, data schema, 
    performance metrics, and environment versions for model governance.
    """
    return {
        "created_at": datetime.now(timezone.utc).isoformat(),
        "target": config.target_column,
        "features": {
            "numeric": list(config.numeric_features),
            "total_count": len(config.numeric_features),
        },
        "dataset": {
            "rows": int(len(dataset)),
            "columns": int(len(dataset.columns)),
        },
        "model": {
            "algorithm": "LinearSVC",
            "hyperparameters": {
                "loss": "squared_hinge",
                "C": 0.005,
                "class_weight": "balanced",
                "fit_intercept": True,
                "dual": False,
                "random_state": config.random_state,
                "test_size": config.test_size,
                "cv_folds": config.cv_folds,
            },
        },
        "metrics": metrics,
        "environment": {
            "python": sys.version,
            "platform": platform.platform(),
            "numpy": np.__version__,
            "pandas": pd.__version__,
            "scikit_learn": sklearn.__version__,
        },
    }

# ============================================================
# ARTIFACT STORAGE
# ============================================================

def save_artifacts(
    model: Pipeline,
    metadata: dict[str, Any],
    config: Config,
) -> None:
    """
    Save the trained ML pipeline and model metadata to disk.
    """
    config.artifact_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    model_path = config.artifact_dir / config.model_filename
    metadata_path = config.artifact_dir / config.metadata_filename

    joblib.dump(model, model_path, compress=3)

    with metadata_path.open("w", encoding="utf-8") as file:
        json.dump(
            metadata,
            file,
            indent=2,
        )

    logger.info("Model saved to %s", model_path)
    logger.info("Metadata artifact saved to %s", metadata_path)

# ============================================================
# TRAINING
# ============================================================

def train(
    data: pd.DataFrame,
    config: Config,
) -> tuple[Pipeline, dict[str, float]]:
    """
    Train ML pipeline with validation, stratified splitting, cross-validation, 
    final evaluation, and artifact storage.
    """
    # 1. Data Validation
    validate_dataset(data, config)

    X = data[list(config.numeric_features)]
    y = data[config.target_column]

    # 2. Stratified Data Split
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=config.test_size,
        random_state=config.random_state,
        stratify=y,
    )

    logger.info(
        "Train rows=%d | Test rows=%d",
        len(X_train),
        len(X_test),
    )

    # 3. Build Pipeline & Cross-Validate
    model = build_pipeline(config)

    logger.info(
        "Running %d-fold cross-validation...",
        config.cv_folds,
    )

    cv_metrics = cross_validate_model(
        model,
        X_train,
        y_train,
        config,
    )

    logger.info(
        "CV F1: %.4f ± %.4f",
        cv_metrics.get("f1_mean", 0.0),
        cv_metrics.get("f1_std", 0.0),
    )

    # 4. Train Final Model on Train Split
    logger.info("Training final model pipeline...")
    model.fit(X_train, y_train)

    # 5. Evaluate on Unseen Test Split
    test_metrics = evaluate_classifier(
        model,
        X_test,
        y_test,
    )

    logger.info(
        "Test metrics: %s",
        test_metrics,
    )

    # 6. Combine CV and Test Metrics
    metrics = {
        **cv_metrics,
        **{
            f"test_{key}": value
            for key, value in test_metrics.items()
        },
    }

    # 7. Generate Metadata & Save Artifacts
    metadata = build_metadata(
        config, 
        metrics, 
        data
    )  

    save_artifacts(  
        model,
        metadata,
        config,
    )

    return model, metrics

# ============================================================
# ENTRY POINT
# ============================================================

def main() -> None:

    url = (
        "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%203/data/creditcard.csv"
    )

    logger.info("Loading dataset...")

    data = pd.read_csv(url)

    train(
        data=data,
        config=CONFIG,
    )

if __name__ == "__main__":
    main()