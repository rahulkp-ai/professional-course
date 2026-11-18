import pandas as pd

data = [
    [4,2,1],
    [3,0,1],
    [1,0,0]
]

columns = ['apple', 'bananas', 'oranges']
index = ['Monday','Tuesday', 'Wednesday']

df = pd.DataFrame(data, index, columns)
print(df)