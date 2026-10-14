from __future__ import annotations

import logging
from sklearn.datasets import load_iris

from config import CONFIG
from train import train

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)

logger = logging.getLogger("knn_main")


def main() -> None:
    logger.info("Loading Iris dataset...")

    # Load standard iris dataset as a pandas DataFrame
    iris_raw = load_iris(as_frame=True)
    data = iris_raw.frame

    train(
        data=data,
        config=CONFIG,
    )


if __name__ == "__main__":
    main()