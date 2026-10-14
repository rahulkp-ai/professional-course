from __future__ import annotations

import json
import logging
import platform
import sys
from datetime import datetime, timezone
from typing import Any

import joblib
import numpy as np
import pandas as pd
import sklearn

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

from config import Config
from model import build_pipeline
from preprocessor import validate_dataset

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)

logger = logging.getLogger("knn_training")


def evaluate_classifier(
    model: Pipeline,
    X_test: pd.DataFrame,
    y_test: pd.Series | np.ndarray,
) -> dict[str, float]:
    """
    Evaluate a classifier for multi-class or binary targets.
    """
    predictions = model.predict(X_test)

    is_multiclass = len(np.unique(y_test)) > 2
    average_mode = "macro" if is_multiclass else "binary"

    metrics = {
        "accuracy": float(
            accuracy_score(y_test, predictions)
        ),
        "precision": float(
            precision_score(
                y_test,
                predictions,
                average=average_mode,
                zero_division=0,
            )
        ),
        "recall": float(
            recall_score(
                y_test,
                predictions,
                average=average_mode,
                zero_division=0,
            )
        ),
        "f1": float(
            f1_score(
                y_test,
                predictions,
                average=average_mode,
                zero_division=0,
            )
        ),
    }

    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba(X_test)
        try:
            if is_multiclass:
                metrics["roc_auc"] = float(
                    roc_auc_score(y_test, probabilities, multi_class="ovr", average="macro")
                )
            else:
                metrics["roc_auc"] = float(
                    roc_auc_score(y_test, probabilities[:, 1])
                )
        except Exception as e:
            logger.warning("Could not calculate ROC-AUC: %s", e)
    else:
        logger.warning("Model lacks predict_proba; ROC-AUC skipped.")
        
    return metrics


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

    is_multiclass = len(np.unique(y_train)) > 2
    f1_scoring = "f1_macro" if is_multiclass else "f1"
    precision_scoring = "precision_macro" if is_multiclass else "precision"
    recall_scoring = "recall_macro" if is_multiclass else "recall"

    scoring = {
        "accuracy": "accuracy",
        "precision": precision_scoring,
        "recall": recall_scoring,
        "f1": f1_scoring,
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

    cv_metrics = {}

    for metric in scoring:
        values = results[f"test_{metric}"]
        cv_metrics[f"{metric}_mean"] = float(np.mean(values))
        cv_metrics[f"{metric}_std"] = float(np.std(values))
        
    return cv_metrics


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
            "algorithm": "KNeighborsClassifier",
            "hyperparameters": {
                "n_neighbors": config.n_neighbors,
                "weights": "distance",
                "metric": "euclidean",
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


def train(
    data: pd.DataFrame,
    config: Config,
) -> tuple[Pipeline, dict[str, float]]:
    """
    Train ML pipeline with validation, stratified splitting, cross-validation, 
    final evaluation, and artifact storage.
    """
    validate_dataset(data, config)

    X = data[list(config.numeric_features)]
    y = data[config.target_column]

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
        "CV F1 (Macro): %.4f ± %.4f",
        cv_metrics.get("f1_mean", 0.0),
        cv_metrics.get("f1_std", 0.0),
    )

    logger.info("Training final model pipeline...")
    model.fit(X_train, y_train)

    test_metrics = evaluate_classifier(
        model,
        X_test,
        y_test,
    )

    logger.info(
        "Test metrics: %s",
        test_metrics,
    )

    metrics = {
        **cv_metrics,
        **{
            f"test_{key}": value
            for key, value in test_metrics.items()
        },
    }

    metadata = build_metadata(config, metrics, data)  
    save_artifacts(model, metadata, config)

    return model, metrics