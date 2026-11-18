import pandas as pd

# Use the raw.githubusercontent.com link instead of the github.com/blob/ link
csv_url = "https://raw.githubusercontent.com/paiml/wine-ratings/main/wine-ratings.csv"

df = pd.read_csv(csv_url, index_col=0)
print(df.head(10))