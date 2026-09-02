import os
import numpy as np
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent.parent

RAW_DATA_LOC = BASE_DIR / "data" / "raw" / "medical_insurance_dataset.csv"
PRO_DATA_LOC = BASE_DIR / "data" / "processed" / "insurance_cleaned.csv"

def import_dataset(file_path=RAW_DATA):
    """Loads raw medical insurance data, sets standard column headers,

    and handles missing value indicators.
    """
    df = pd.read_csv(file_path)

    headers = [
        "age",
        "gender",
        "bmi",
        "no_of_children",
        "smoker",
        "region",
        "charges",
    ]
    df.columns = headers
    df.replace("?", np.nan, inplace=True)

    return df


if __name__ == "__main__":
    df = import_dataset()
    print(df.head(10))