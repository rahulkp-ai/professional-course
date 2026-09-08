import logging
from typing import Tuple

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, log_loss
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Configure structured logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def load_data(url: str) -> pd.DataFrame:
    """Fetch churn dataset from a remote URL."""
    try:
        df = pd.read_csv(url)
        logging.info("Dataset successfully loaded. Shape: %s", df.shape)
        return df
    except Exception as e:
        logging.error("Failed to load data from %s: %s", url, e)
        raise


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """Select core features and format target variable explicitly."""
    feature_cols = [
        "tenure",
        "age",
        "address",
        "income",
        "ed",
        "employ",
        "equip",
        "churn",
    ]

    # Create an explicit copy to prevent SettingWithCopyWarning
    churn_df = df[feature_cols].copy()
    churn_df["churn"] = churn_df["churn"].astype(int)

    logging.info("Preprocessing complete. Target class counts:\n%s", churn_df["churn"].value_counts().to_dict())

    return churn_df

def feature_matrix(df: pd.DataFrame) -> pd.DataFrame:
    churn_df        = df
    input_feilds    = [
                        "tenure",
                        "age",
                        "address",
                        "income",
                        "ed",
                        "employ",
                        "equip",
                        ]
    X               =   np.asarray(churn_df[input_feilds])
    logging.info("Feature selection sussfull")
    print(X[0:5])
    return X

def target_variable(df: pd.DataFrame) -> pd.DataFrame:
    out_put_feild   =   ['churn']
    churn_df        = df
    y               = np.asarray(churn_df[out_put_feild])
    logging.info("seting target variable sussfull")
    print(y[0:5])
    return y

def normalize_dataset(X: np.ndarray) -> Tuple[np.ndarray, StandardScaler]:
    """Normalize features and return both normalized matrix and fitted scaler."""
    scaler = StandardScaler()
    X_normalized = scaler.fit_transform(X)
    return X_normalized, scaler

def split_dataset(
        X: np.ndarray, 
        y: np.ndarray, 
        test_size: float = 0.2, 
        random_state: int = 4
    ) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    
    """Split normalized feature matrix and target array into training and test sets."""
    

    X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=random_state
        )

    logging.info(
        "Train set shape: %s, %s | Test set shape: %s, %s",
        X_train.shape,
        y_train.shape,
        X_test.shape,
        y_test.shape,
    )

    return X_train, X_test, y_train, y_test

def train_and_predict_model(
    X_train: np.ndarray, 
    y_train: np.ndarray, 
    X_test: np.ndarray,
    C: float = 0.01,
    solver: str = "liblinear"
) -> Tuple[LogisticRegression, np.ndarray, np.ndarray]:
    """
    Train a Logistic Regression model and output class predictions and probabilities.
    
    Returns:
        Tuple containing (fitted_model, yhat, yhat_prob)
    """

    LR = LogisticRegression(C=C, solver=solver).fit(X_train, y_train.ravel())


    yhat = LR.predict(X_test)
    yhat_prob = LR.predict_proba(X_test)

    # Logging sample output
    logging.info("First 10 predictions: %s", yhat[:10])
    logging.info("First 10 prediction probabilities:\n%s", yhat_prob[:10])


    return LR, yhat, yhat_prob

def plot_feature_importance(
    model: LogisticRegression, 
    feature_names: list
) -> None:
    """Plot horizontal bar chart of feature coefficients from a trained Logistic Regression model."""
    
    
    coefficients = pd.Series(model.coef_[0], index=feature_names)


    plt.figure(figsize=(8, 5))
    coefficients.sort_values().plot(kind="barh", color="skyblue", edgecolor="black")
    
    plt.title("Feature Coefficients in Logistic Regression Churn Model")
    plt.xlabel("Coefficient Value")
    plt.grid(axis="x", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.show()

def evaluate_performance(y_test: np.ndarray, yhat_prob: np.ndarray, yhat: np.ndarray = None) -> float:
    """Calculate log loss (and optionally report classification metrics)."""
    
    loss = log_loss(y_test, yhat_prob)
    logging.info("Log Loss: %.4f", loss)

    if yhat is not None:
        acc = accuracy_score(y_test, yhat)
        logging.info("Accuracy: %.4f", acc)
        logging.info("\nClassification Report:\n%s", classification_report(y_test, yhat))


    return loss

def predict_from_user_input(
        model: LogisticRegression,
        scaler: StandardScaler,
        feature_names: list
    ) -> Tuple[int, float]:
    """
    Prompt the user via CLI to input feature values, scale them using the fitted scaler,
    and predict churn class and probability.
    """
    print("\n--- Enter Feature Values for Churn Prediction ---")
    user_inputs = []

    # Prompt user for each feature step-by-step with validation
    for feature in feature_names:
        while True:
            try:
                val = float(input(f"Enter value for '{feature}': "))
                user_inputs.append(val)
                break
            except ValueError:
                print("Invalid input! Please enter a valid numerical value.")

    # Convert user input list to 2D array: shape (1, n_features)
    raw_feature_matrix = np.array([user_inputs])

    # Highlighted Fix: Scale using transform() with the ALREADY fitted scaler (do NOT fit again)
    normalized_feature_matrix = scaler.transform(raw_feature_matrix)

    # Make predictions
    prediction = int(model.predict(normalized_feature_matrix)[0])
    probabilities = model.predict_proba(normalized_feature_matrix)[0]
    churn_probability = float(probabilities[1])

    # Output formatted results
    print("\n" + "=" * 40)
    print("PREDICTION RESULT")
    print("=" * 40)
    print(f"Churn Prediction : {prediction} ({'Churn' if prediction == 1 else 'No Churn'})")
    print(f"Churn Probability: {churn_probability:.2%}")
    print("=" * 40)

    return prediction, churn_probability

def sample_data(df: pd.DataFrame):
    sample  =   df
    print(sample.head(10))


if __name__ == "__main__":
    
    DATA_URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%203/data/ChurnData.csv"
    
    input_fields = ["tenure", "age", "address", "income", "ed", "employ", "equip"]

    # Execution Pipeline
    raw_df = load_data(DATA_URL)
    clean_df = preprocess_data(raw_df)

    X = feature_matrix(clean_df)
    y = target_variable(clean_df)
    X_normalized, fitted_scaler = normalize_dataset(X)

    X_train, X_test, y_train, y_test = split_dataset(X_normalized, y)
    
    LR, yhat, yhat_prob = train_and_predict_model(X_train, y_train, X_test)
    
    plot_feature_importance(LR, feature_names=input_fields)
    
    loss = evaluate_performance(y_test, yhat_prob, yhat)

    pred, prob = predict_from_user_input(
        model=LR, 
        scaler=fitted_scaler, 
        feature_names=input_fields
    )




