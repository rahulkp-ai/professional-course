from pathlib import Path
import numpy as np
import pandas as pd

# Resolve the root directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent.parent

RAW_DATA_LOC = BASE_DIR / "data" / "raw" / "medical_insurance_dataset.csv"
PRO_DATA_LOC = BASE_DIR / "data" / "processed" / "insurance_cleaned.csv"


def import_dataset(file_path=RAW_DATA_LOC):
    """Loads raw medical insurance data, sets standard column headers,

    and handles missing value indicators.
    """
    df      = pd.read_csv(file_path)

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

def data_wrangling(file_path=RAW_DATA_LOC):
    """Cleans raw dataset by imputing missing values and adjusting column data types.

    Fills missing 'smoker' values with the mode and missing 'age' values with the 
    mean, then converts both columns to integer data types.
    """
    
    df              = import_dataset()
    is_smoker       = df['smoker'].value_counts().idxmax()
    df['smoker']    = df['smoker'].fillna(is_smoker)
    age_mean        = df['age'].astype(float).mean()
    df['age']       = df['age'].fillna(age_mean)
    df['age']       = df['age'].astype(int)
    df['smoker']    = df['smoker'].astype(int)
    
    return df

def save_dataset(df,output_file=PRO_DATA_LOC):
    """Saves the processed DataFrame to a CSV file.
    Creates target directories if they do not exist and excludes the default Pandas index.
    """
    output_path =   Path(output_file)
    output_path.parent.mkdir(parents=True,exist_ok=True)
    df.to_csv(output_path,index=False)
    print(f"Dataset successfully saved to: {output_path}")


if __name__ == "__main__":
    df = data_wrangling()
    save_dataset(df)