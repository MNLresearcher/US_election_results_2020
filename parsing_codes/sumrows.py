import pandas as pd

data = pd.read_csv('.csv')

df = data.groupby(['county','candidate']).sum()
# summing up the rows (sometimes they divide the total votes of each candidate into 'early votes', 'election day', and 'absentee votes')
 
df.to_csv('.csv', index=False)