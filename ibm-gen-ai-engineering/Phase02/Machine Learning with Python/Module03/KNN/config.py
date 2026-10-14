from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Config:
    random_state: int = 42
    test_size: float = 0.20
    cv_folds: int = 5
    n_neighbors: int = 4

    BASE_DIR = Path(__file__).resolve().parent
    artifact_dir: Path = BASE_DIR / "artifacts"
    model_filename: str = "knn_model.joblib"
    metadata_filename: str = "metadata.json"

    target_column: str = "target"
    
    numeric_features: tuple[str, ...] = (
        "sepal length (cm)",
        "sepal width (cm)",
        "petal length (cm)",
        "petal width (cm)",
    )


CONFIG = Config()