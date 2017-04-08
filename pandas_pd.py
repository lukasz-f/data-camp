import pandas as pd

brics = pd.read_csv("brics.csv", index_col=0)  # Load csv file contains labels in first row
print(brics)
print('---')
print(brics['country'])  # Column as Pandas Series
print(brics[['country']])  # Column as Pandas DataFrame
print(brics.country)  # Column access with dot notation
print('---')
brics['on_earth'] = [True, True, True, True, True]  # Add column
print(brics)
print('---')
brics['density'] = brics['population'] / brics['area'] * 1000000  # Add column based on other columns
print(brics)
print('---')
print(brics.loc['BR'])  # Label-based row access
print(brics.loc[['BR', 'CH']])  # Rows as Pandas DataFrame
print('---')
print(brics.loc['CH', 'capital'])  # Element access
print(brics['capital'].loc['CH'])
print(brics.loc['CH']['capital'])
print('---')
print(brics.loc[['BR', 'CH'], ['population', 'area']])  # Sub-DataFrame
