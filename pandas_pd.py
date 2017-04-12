import pandas as pd

brics = pd.read_csv("brics.csv", index_col=0)  # Load csv file contains labels in first row
brics

brics['country']  # Column as Pandas Series
brics[['country']]  # Column as Pandas DataFrame
brics.country  # Column access with dot notation
brics.get('country')  # Column access

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

# Create DataFrame from dictionary
frame_dict = pd.DataFrame(
    {"A": [1, 2, 3, 4, 5],
     "B": ["k", None, "k","m", "k"],
     "C": [False, True, True, False, False]
    })
frame_dict

# Create DataFrame from list with columns name and index name
frame_array = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=["A", "B", "C"], index=['a', 'b', 'c'])
frame_array

# Create Series
series_array = pd.Series([1, 2, 3, 4])
series_array
