import logging
from pathlib import Path
from typing import Dict, Tuple, Any

import joblib
import pandas as pd
import numpy as np

# Set non-interactive Matplotlib backend BEFORE importing pyplot
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report

# Configure structured logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("DrugClassificationPipeline")


# -------------------------------------------------------------------
# 1. DATA INGESTION
# -------------------------------------------------------------------
def load_data(url: str) -> pd.DataFrame:
    """Loads dataset from URL or file path with validation."""
    try:
        df = pd.read_csv(url)
        if df.empty:
            raise ValueError("Dataset is empty.")
        logger.info("Successfully loaded dataset. Shape: %s", df.shape)
        return df
    except Exception as e:
        logger.error("Failed to load dataset from %s: %s", url, e, exc_info=True)
        raise


# -------------------------------------------------------------------
# 2. EXPLORATORY DATA ANALYSIS & REPORTING
# -------------------------------------------------------------------
def generate_data_analysis(data: pd.DataFrame, report_path: Path) -> Path:
    """Generates feature summary statistics and exports report to CSV."""
    if data is None or data.empty:
        raise ValueError("Cannot perform data analysis on empty DataFrame.")

    try:
        report_path.parent.mkdir(parents=True, exist_ok=True)
        summary = data.describe(include="all").transpose()
        summary["missing_values"] = data.isnull().sum()
        summary["data_types"] = data.dtypes
        summary.to_csv(report_path)
        logger.info("Saved data analysis report to: %s", report_path)
        return report_path
    except Exception as e:
        logger.error("Failed to generate data analysis: %s", e, exc_info=True)
        raise


def plot_category_distribution(
    data: pd.DataFrame, 
    target_col: str, 
    output_path: Path
) -> Path:
    """Generates categorical feature bar plot and saves to disk without UI popups."""
    if target_col not in data.columns:
        raise ValueError(f"Column '{target_col}' not found in DataFrame.")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(10, 6))

    try:
        category_counts = data[target_col].value_counts()
        ax.bar(
            category_counts.index.astype(str),
            category_counts.values,
            color="royalblue",
            edgecolor="black"
        )
        ax.set_xlabel(target_col, fontsize=12)
        ax.set_ylabel("Count", fontsize=12)
        ax.set_title(f"Target Distribution: {target_col}", fontsize=14)
        ax.tick_params(axis="x", rotation=45)

        fig.savefig(output_path, dpi=300, bbox_inches="tight")
        logger.info("Saved category distribution plot to: %s", output_path)
        return output_path
    except Exception as e:
        logger.error("Failed to generate category distribution plot: %s", e, exc_info=True)
        raise
    finally:
        plt.close(fig)  # Release GPU/CPU memory


# -------------------------------------------------------------------
# 3. FEATURE ENGINEERING & PREPROCESSING
# -------------------------------------------------------------------
def encode_categorical_features(
    data: pd.DataFrame,
    categorical_cols: list[str],
    encoders_save_path: Path
) -> Tuple[pd.DataFrame, Dict[str, LabelEncoder]]:
    """
    Encodes categorical features using LabelEncoder.
    Persists fitted encoders to disk for downstream inference pipelines.
    """
    df = data.copy()
    encoders: Dict[str, LabelEncoder] = {}

    try:
        for col in categorical_cols:
            if col not in df.columns:
                raise KeyError(f"Column '{col}' not found in DataFrame.")
            
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col])
            encoders[col] = le

        encoders_save_path.parent.mkdir(parents=True, exist_ok=True)
        joblib.dump(encoders, encoders_save_path)
        logger.info("Successfully encoded features %s and saved artifacts to: %s", 
                    categorical_cols, encoders_save_path)
        return df, encoders
    except Exception as e:
        logger.error("Failed during categorical feature encoding: %s", e, exc_info=True)
        raise


# -------------------------------------------------------------------
# 4. MODEL TRAINING & EVALUATION
# -------------------------------------------------------------------
def train_decision_tree(
    data: pd.DataFrame,
    target_col: str,
    model_save_path: Path,
    tree_plot_path: Path,
    test_size: float = 0.3,
    random_state: int = 32
) -> Tuple[Path, float]:
    """
    Trains DecisionTreeClassifier, evaluates accuracy, saves tree visualization 
    and exports trained model binary.
    """
    if target_col not in data.columns:
        raise ValueError(f"Target column '{target_col}' missing from training data.")

    try:
        X = data.drop(columns=[target_col])
        y = data[target_col]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=random_state, stratify=y
        )

        clf = DecisionTreeClassifier(
            criterion="entropy", 
            max_depth=4, 
            random_state=random_state
        )
        clf.fit(X_train, y_train)
        logger.info("Model training completed.")

        # Evaluation
        predictions = clf.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        logger.info("Evaluation Complete -> Accuracy Score: %.4f", accuracy)
        logger.debug("Classification Report:\n%s", classification_report(y_test, predictions))

        # Save Model Artifact
        model_save_path.parent.mkdir(parents=True, exist_ok=True)
        joblib.dump(clf, model_save_path)
        logger.info("Saved trained model artifact to: %s", model_save_path)

        # Plot and save Decision Tree structure
        tree_plot_path.parent.mkdir(parents=True, exist_ok=True)
        fig, ax = plt.subplots(figsize=(14, 10))
        plot_tree(
            clf, 
            feature_names=list(X.columns), 
            class_names=[str(c) for c in clf.classes_], 
            filled=True, 
            ax=ax
        )
        fig.savefig(tree_plot_path, dpi=300, bbox_inches="tight")
        plt.close(fig)
        logger.info("Saved decision tree graph to: %s", tree_plot_path)

        return model_save_path, float(accuracy)
    except Exception as e:
        logger.error("Failed model training and evaluation pipeline: %s", e, exc_info=True)
        raise


# -------------------------------------------------------------------
# 5. INFERENCE FUNCTION (Production Ready Payload Tester)
# -------------------------------------------------------------------
def predict_sample(
    raw_payload: dict[str, Any], 
    encoders_path: Path, 
    model_path: Path
) -> str:
    """Transforms raw inference payload and generates prediction using saved artifacts."""
    encoders: Dict[str, LabelEncoder] = joblib.load(encoders_path)
    model: DecisionTreeClassifier = joblib.load(model_path)

    payload_df = pd.DataFrame([raw_payload])

    # Transform categorical fields using saved encoders
    for col, encoder in encoders.items():
        if col in payload_df:
            payload_df[col] = encoder.transform(payload_df[col])

    prediction = model.predict(payload_df)[0]
    return str(prediction)


# -------------------------------------------------------------------
# 6. PIPELINE ORCHESTRATION
# -------------------------------------------------------------------
if __name__ == "__main__":
    # Define Base Directories & Artifact Paths
    BASE_DIR = Path(__file__).resolve().parent
    ARTIFACTS_DIR = BASE_DIR / "artifacts"
    
    REPORTS_DIR = ARTIFACTS_DIR / "reports"
    PLOTS_DIR = ARTIFACTS_DIR / "plots"
    MODELS_DIR = ARTIFACTS_DIR / "models"

    DATA_URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%203/data/drug200.csv"

    # Step 1: Data Ingestion
    raw_data = load_data(DATA_URL)

    # Step 2: Analysis & Visualization
    generate_data_analysis(raw_data, REPORTS_DIR / "data_analysis.csv")
    plot_category_distribution(raw_data, "Drug", PLOTS_DIR / "target_distribution.png")

    # Step 3: Feature Preprocessing
    categorical_cols = ["Sex", "BP", "Cholesterol"]
    encoders_path = MODELS_DIR / "label_encoders.joblib"
    processed_data, _ = encode_categorical_features(
        raw_data, 
        categorical_cols=categorical_cols, 
        encoders_save_path=encoders_path
    )

    # Step 4: Model Training & Evaluation
    model_path = MODELS_DIR / "decision_tree_model.joblib"
    tree_plot_path = PLOTS_DIR / "decision_tree_structure.png"
    
    saved_model_file, final_accuracy = train_and_evaluate_model = train_decision_tree(
        data=processed_data,
        target_col="Drug",
        model_save_path=model_path,
        tree_plot_path=tree_plot_path
    )

    # Step 5: Test Inference Pipeline with Unseen Raw Data
    sample_patient = {
        "Age": 47,
        "Sex": "M",
        "BP": "LOW",
        "Cholesterol": "HIGH",
        "Na_to_K": 10.11
    }
    
    predicted_drug = predict_sample(sample_patient, encoders_path, model_path)
    logger.info("Sample Patient Inference Result -> Prescribed Drug: %s", predicted_drug)