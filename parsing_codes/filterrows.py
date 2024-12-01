import pandas as pd

data = pd.read_csv('.csv')

df = data.loc[data['']=='']
# Filtering the rows you need and deleting the rest

df.to_csv('.csv', index=False)