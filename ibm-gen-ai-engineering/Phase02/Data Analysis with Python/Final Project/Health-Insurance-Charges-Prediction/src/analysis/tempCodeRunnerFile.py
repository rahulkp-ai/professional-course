import pandas as pd
import numpy as np
import seaborn as sns
import pathlib as Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
PRO_DATA_LOC = BASE_DIR / "data"/ "processed" / "insurance_cleaned.csv"

def reg_plot(file_path=PRO_DATA_LOC):
    df = pd.read_csv(file_path)
    sns.regplot(
        x='bmi',
        y='charges',
        data=df,
        line_kws={"color":"red"}
    )
    plt.ylim(0,)
    plt.show()

if __name__ == "__main__":
    reg_plot()
