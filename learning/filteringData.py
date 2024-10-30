import re
import pandas as pd
df = pd.read_csv('pokemon_data.csv') 

#print(df.loc[df['Type 1']=='Grass'])
#print(df.loc[(df['Type 1']=='Grass') & (df['Type 2'] == 'Poison')] )

#new_df = df.loc[(df['Type 1']=='Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)] 
#new_df = new_df.reset_index()
#new_df.to_csv('filtered.csv')

print(df.loc[df['Type 1'].str.contains('Fire|Grass', regex=True)])

print(df.loc[df['Name'].str.startswith("Pi")])