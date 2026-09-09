import logging
from typing import Tuple
from pathlib import Path
import joblib

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsOneClassifier
from sklearn.metrics import accuracy_score

# Configure structured logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

def load_data(url: str) -> pd.DataFrame:
    """Fetch Obesity dataset from a remote URL."""
    try:
        df  =   pd.read_csv(url)
        logging.info("dataset successfully loaded")
        return df
    except Exception as e:
        logging.error("Failed to load data from %s: %s:", url, e)
        raise

def generate_distribution_plot(
    df: pd.DataFrame,
    target_col: str = "NObeyesdad",
    filename: str | Path = "obesity_distribution.png"
    )  -> Path:
    """Generates and saves a count plot for the specified target variable."""

    if df.empty:
        raise ValueError("DataFrame is empty")
    
    if target_col not in df:
        raise KeyError(f"column '{target_col}' not found in DataFrame")
    

    script_dir = Path(__file__).resolve().parent
    out_put_file = script_dir / filename
    
    fig, ax = plt.subplots(figsize=(10,6))

    try:
        sns.countplot(
            data = df,
            x = target_col,
            ax = ax,
            order = df[target_col].value_counts().index
        )

        ax.set_title("Distribution of Obesity Levels", fontsize=14, fontweight="bold")
        ax.set_xlabel("Obesity Level", fontsize=12)
        ax.set_ylabel("Count", fontsize=12)
        ax.tick_params(axis="x", rotation=45)

        fig.tight_layout()
        fig.savefig(out_put_file, dpi=300, bbox_inches="tight")
        logging.info("Plot successfully saved to %s", out_put_file.resolve())
        
        return out_put_file.resolve()

    finally:
        plt.close(fig)

def EDA(df: pd.DataFrame) -> tuple:
    
    if df.empty:
        raise ValueError("Dataset is empty")
    
    try:
        null    = df.isnull().sum()
        summary = df.describe()
        info    = df.info()
        logging.info("successfull EDA")
        return null, summary, info
    except Exception as e:
        logging.error("Failed to EDA %s:",e)
        raise

def data_Preprocessing_Features_Scaling(
    data: pd.DataFrame) -> pd.DataFrame:
    """Scale the numerical features to standardize their ranges for better model performance."""
    """One-hot encoding Convert categorical variables into numerical format using one-hot encoding."""
    
    if data.empty:
        raise ValueError("Datset is empty")
    
    # Features Scaling 
    try:
        continuous_columns = data.select_dtypes(
            include=['float64']).columns.tolist()
        scalar  = StandardScaler()
        scaled_features =   scalar.fit_transform(data[continuous_columns])
        scaled_df   =   pd.DataFrame(
            scaled_features, 
            columns=scalar.get_feature_names_out(continuous_columns),
            index=data.index
            )
        scaled_data = pd.concat([data.drop(
            columns=continuous_columns), 
            scaled_df], 
            axis=1)
        logging.info("successfull feature scaling")
        return scaled_data
    except Exception as e:
        logging.error("failed to feature scaling %s:",e)
        raise

def  data_Preprocessing_One_hot_encoding(
    scaled_data: pd.DataFrame) -> pd.DataFrame:  
    #One-hot encoding
    try:
        categorical_columns =   scaled_data.select_dtypes(include=['object']).columns.tolist()
        categorical_columns.remove('NObeyesdad')

        encoder     =   OneHotEncoder(
            sparse_output=False, 
            drop='first')
        encoder = OneHotEncoder(
            sparse_output=False, 
            drop='first')
        encoded_features = encoder.fit_transform(scaled_data[categorical_columns])

        encoded_df  = pd.DataFrame(
            encoded_features,
            columns=encoder.get_feature_names_out(
                categorical_columns),
                index=scaled_data.index
            )
        prepped_data = pd.concat([scaled_data.drop(
            columns=categorical_columns),
            encoded_df], 
            axis=1
            )
        logging.info("successfull One-hot encoding")
        return prepped_data
    except Exception as e:
        logging.error("failed One-hot encoding %s", e)
        raise

def encode_target_variable(
    prepped_data: pd.DataFrame, 
    target: str = "NObeyesdad") -> pd.DataFrame:
    
    if prepped_data.empty:
        raise ValueError("Dataset is empty")

    try:
        prepped_data[target] = prepped_data[target].astype('category').cat.codes
        logging.info("successfully target variable encoding")
        return prepped_data
    except Exception as e:
        logging.error("failed target variable encoding")

def set_input_and_target(prepped_data: pd.DataFrame) -> tuple:
    
    if prepped_data.empty:
        raise ValueError("Dataset is empty")
    
    try:
        X = prepped_data.drop('NObeyesdad', axis=1)
        y = prepped_data['NObeyesdad']
        logging.info("successfully set input and target, X,y")
        return X, y
    except Exception as e:
        logging.error("failed setting input and target, X,y")
        raise

def split_dataset(
    X: pd.DataFrame,
    y: pd.Series | pd.DataFrame,
    test_size: float =0.2,
    stratify= None,
    random_state: int = 42
    ) -> tuple:
    """Split features and target into training and testing sets."""

    if X.empty or y.empty:
        raise ValueError("Dataset is empty")
    
    if stratify is None:
        stratify = y
    
    try:
        X_train, X_test, y_train, y_test    =   train_test_split(
            X,
            y,
            test_size=test_size,
            stratify=stratify,
            random_state=random_state
        )
        logging.info("successfully split dataset")
        return X_train, X_test, y_train, y_test
    
    except Exception as e:
        logging.error("failed split dataset %s", e)
        raise

def model_OVA_train(
    X_train: pd.DataFrame,
    y_train: pd.Series | pd.DataFrame,
    filepath: str | Path = "model_ove.joblib"
    ) -> tuple:
    """Train a One-vs-Rest (OVA) Logistic Regression model and save it to disk."""

    script_dir = Path(__file__).resolve().parent
    out_put_file = script_dir / filepath

    if X_train.empty or y_train.empty:
        raise ValueError("Dataset is empty")

    try:
        model_ova = LogisticRegression(
            multi_class='ovr', 
            max_iter=1000,
            random_state=42
            )

        model_ova.fit(X_train, y_train)
        logging.info("successfully model OVA trained")

        joblib.dump(model_ova,out_put_file)
        logging.info("successfully model OVA saved to %s:", out_put_file)

        return model_ova, out_put_file

    except Exception as e:
        logging("failed to train model OVA training %s",e)
        raise

def model_OVA_predict(
    model_path: str | Path,
    X_test: pd.DataFrame,
    ) -> np.ndarray:

    """Loads a saved joblib model and predicts target values for test data."""

    if X_test.empty:
        raise ValueError("X_test is empty")

    path = Path(model_path)

    if not path.exists():
        raise FileNotFoundError(f"Model file not found at: {path.resolve()}")

    try:
        model_ova = joblib.load(path)
        logging.info("successfully loaded model") 

        prediction = model_ova.predict(X_test)
        logging.info("successfully model predict")
        return prediction
    except Exception as e:
        logging.error("Failed to generate predictions: %s", e) 

def model_OVA_accuracy(
    y_test: pd.Series | pd.DataFrame,
    y_pred_ova: np.ndarray 
    ) -> float:

    if y_test.empty:
        raise ValueError("y_test is empty")
    
    try:
        accuracy = np.round(100*accuracy_score(y_test,y_pred_ova),2)
        logging.info("successfully ealuvated accuracy")
        return accuracy
    except Exception as e:
        logging.error("failed to evaluvate accuuracy")

if __name__ == "__main__":
    
    DATA_URL    =   "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/GkDzb7bWrtvGXdPOfk6CIg/Obesity-level-prediction-dataset.csv"
    url   = "/Users/rahulkpkurup/Learning/ML-Git-Portfolio/professional-course/ibm-gen-ai-engineering/Phase02/Machine Learning with Python/Module03/Classification/model_ove.joblib"
    raw_data    =   load_data(DATA_URL)
    generate_distribution_plot(raw_data,target_col='NObeyesdad')
    EDA(raw_data)
    scaled_data = data_Preprocessing_Features_Scaling(raw_data)
    prepped_data  = data_Preprocessing_One_hot_encoding(scaled_data)
    encoded_target  = encode_target_variable(prepped_data)
    X,y    =    set_input_and_target(prepped_data)
    X_train,X_test,y_train,y_test   = split_dataset(X,y)
    model, url = model_OVA_train(X_train, y_train)
    MODEL_URL   = url
    y_pred_ova = model_OVA_predict(MODEL_URL, X_test)
    accuracy = model_OVA_accuracy(y_test,y_pred_ova)
    print(accuracy,"%")