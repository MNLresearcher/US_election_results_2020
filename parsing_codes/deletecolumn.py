import pandas as pd

data = pd.read_csv('.csv')

data.drop([], inplace= True, axis=1)
#Removing the unwanted columns

#data.sort_values(by=['candidate'], axis=0, inplace=False, ascending=True)

data.to_csv('.csv', index=False)