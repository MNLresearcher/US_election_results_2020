import pandas as pd

data = pd.read_csv('.csv')

df = data.melt(id_vars='county', var_name='candidate', value_name='votes')
# If the columns are the candidate's names and they contain their respective votes, we switch them to index names

df.to_csv('.csv', index=False)