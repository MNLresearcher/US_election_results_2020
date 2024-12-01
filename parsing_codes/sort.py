import pandas as pd

data = pd.read_csv('.csv')

df = data.sort_values(by='', ascending=True)
# If you just want to rearrange the row after one column

df.to_csv('.csv', index= False)