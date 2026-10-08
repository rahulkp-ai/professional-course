from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any

import joblib
import numpy as np
import pandas as pd

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)
logger = logging.getLogger("svm_fraud_inference")

# Define Paths matching svm.py artifacts
BASE_DIR = Path(__file__).resolve().parent
ARTIFACTS_DIR = BASE_DIR / "artifacts"
MODEL_PATH = ARTIFACTS_DIR / "svm_model.joblib"
METADATA_PATH = ARTIFACTS_DIR / "metadata.json"

# Realistic default values for Credit Card Fraud features (V1-V28 PCA features + Amount)
DEFAULT_INPUTS: dict[str, str] = {
    "V1": "-1.359807",
    "V2": "-0.072781",
    "V3": "2.536347",
    "V4": "1.378155",
    "V5": "-0.338321",
    "V6": "0.462388",
    "V7": "0.239599",
    "V8": "0.098698",
    "V9": "0.363787",
    "V10": "0.090794",
    "V11": "-0.551600",
    "V12": "-0.617801",
    "V13": "-0.991390",
    "V14": "-0.311169",
    "V15": "1.468177",
    "V16": "-0.470401",
    "V17": "0.207971",
    "V18": "0.025791",
    "V19": "0.403993",
    "V20": "0.251412",
    "V21": "-0.018307",
    "V22": "0.277838",
    "V23": "-0.110474",
    "V24": "0.066928",
    "V25": "0.128539",
    "V26": "-0.189115",
    "V27": "0.133558",
    "V28": "-0.021053",
    "Amount": "149.62",
}


def load_artifacts() -> tuple[Any, list[str]]:
    """Load the trained scikit-learn pipeline and expected feature list."""
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")
    if not METADATA_PATH.exists():
        raise FileNotFoundError(f"Metadata file not found at {METADATA_PATH}")

    model = joblib.load(MODEL_PATH)

    with METADATA_PATH.open("r", encoding="utf-8") as file:
        metadata = json.load(file)

    numeric_features = metadata["features"]["numeric"]
    logger.info("Loaded SVM pipeline from %s", MODEL_PATH)
    return model, numeric_features


def parse_numeric_value(raw_val: str) -> float:
    """Clean string (remove $, commas, spaces) and parse to float."""
    cleaned = raw_val.strip().replace(",", "").lstrip("$")
    return float(cleaned)


def collect_user_inputs(expected_features: list[str]) -> dict[str, float]:
    """Interactively ask user for each transaction feature via console input."""
    print("\n" + "=" * 60)
    print(" CREDIT CARD FRAUD DETECTOR - TRANSACTION FEATURE INPUTS")
    print(" (Press ENTER to accept default values for testing)")
    print("=" * 60 + "\n")

    user_data: dict[str, float] = {}

    for feature in expected_features:
        default_val = DEFAULT_INPUTS.get(feature, "0.0")

        while True:
            raw_input = input(f"Enter {feature} [default: {default_val}]: ").strip()

            # If user presses Enter, use default value
            if not raw_input:
                raw_input = default_val

            try:
                numeric_val = parse_numeric_value(raw_input)
                user_data[feature] = numeric_val
                break
            except ValueError:
                print(
                    f"Invalid input: '{raw_input}'. Please enter a valid floating-point number.\n"
                )

    return user_data


def predict_from_dict(
    input_data: dict[str, float],
    model: Any,
    expected_features: list[str],
) -> tuple[int, float]:
    """
    Predict binary class (0: Legitimate, 1: Fraud) and calculate decision score margin.
    """
    df_input = pd.DataFrame([input_data])[expected_features]
    
    # Get discrete prediction class (0 or 1)
    prediction = int(model.predict(df_input)[0])
    
    # Extract decision function score margin
    if hasattr(model, "decision_function"):
        decision_score = float(model.decision_function(df_input)[0])
    else:
        decision_score = 0.0

    return prediction, decision_score


def main() -> None:
    # 1. Load trained SVM pipeline and metadata
    model, expected_features = load_artifacts()

    # 2. Interactively collect transaction features
    user_inputs = collect_user_inputs(expected_features)

    # 3. Perform Classification Inference
    prediction, decision_score = predict_from_dict(
        user_inputs, model, expected_features
    )

    # 4. Display Inference Result
    print("\n" + "=" * 60)
    print(" TRANSACTION RISK EVALUATION RESULT")
    print("=" * 60)
    
    if prediction == 1:
        print(" STATUS        : FRAUDULENT TRANSACTION DETECTED")
        print(f" DECISION SCORE: {decision_score:+.4f} (Above decision boundary)")
        print(" ACTION        : Flag for immediate verification / Freeze card")
    else:
        print(" STATUS        : LEGITIMATE TRANSACTION")
        print(f" DECISION SCORE: {decision_score:+.4f} (Below decision boundary)")
        print(" ACTION        : Approve transaction")

    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()