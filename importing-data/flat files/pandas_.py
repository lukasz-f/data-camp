# Import pandas as pd
import pandas as pd

# Assign the filename
file = 'titanic_sub.csv'

# Read the file into a DataFrame
df = pd.read_csv(file)

# View the head of the DataFrame
df.head()


# Assign the filename
file = 'mnist_kaggle_some_rows.csv'

# Read the first 5 rows of the file into a DataFrame
data = pd.read_csv(file, nrows=5, header=None)

# Build a numpy array from the DataFrame
data_array = data.values

# Print the datatype of data_array to the shell
print(type(data_array))


# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Assign filename
file = 'titanic_corrupt.txt'

# Import corrupted file with comment at the end of line and 'Nothing' str instead of NaN
data = pd.read_csv(file, sep='\t', comment='#', na_values=['Nothing'])

# Print the head of the DataFrame
print(data.head())

# Plot 'Age' variable in a histogram
pd.DataFrame.hist(data[['Age']])
plt.xlabel('Age (years)')
plt.ylabel('count')
plt.show()
