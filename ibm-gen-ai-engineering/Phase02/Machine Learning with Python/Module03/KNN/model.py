from __future__ import annotations

from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline

from config import Config
from preprocessor import build_preprocessor


def build_model(config: Config) -> KNeighborsClassifier:
    """
    Instantiate K-Nearest Neighbors classifier using distance weighting
    to mitigate class skew bias in majority voting.
    """
    return KNeighborsClassifier(
        n_neighbors=config.n_neighbors,
        weights="distance",
        metric="euclidean",
        algorithm="auto",
        n_jobs=-1,
    )


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