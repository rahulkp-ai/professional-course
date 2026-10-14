from __future__ import annotations

import logging
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from config import Config

logger = logging.getLogger("knn_training")


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


def build_preprocessor(
    config: Config,
) -> ColumnTransformer:
    """
    Build preprocessing that can safely be fitted inside 
    a model Pipeline to prevent train/test preprocessing leakage. 
    KNN specifically requires feature standardization so large scales 
    don't dominate the distance metric.
    """
    numeric_pipeline = Pipeline(
        steps=[
            (
                "imputer",
                SimpleImputer(strategy="median"),
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
                list(config.numeric_features),
            )
        ],
        remainder="drop",
    )