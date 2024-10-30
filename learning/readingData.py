import pandas as pd
df = pd.read_csv('pokemon_data.csv') 

##Read Headers
print(df.columns)

##Read each Column
print(df['Name'][0:5])

##Read each Row
print(df.iloc[1])