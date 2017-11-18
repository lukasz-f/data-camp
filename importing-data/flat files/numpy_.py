# Import package
import numpy as np
import matplotlib.pyplot as plt

# Assign filename to variable
file = 'mnist_kaggle_some_rows.csv'

# Load file as array: digits
digits = np.loadtxt(file, delimiter=',')

# Print datatype of digits
print(type(digits))

# Select and reshape a row
im = digits[21, 1:]
im_sq = np.reshape(im, (28, 28))

# Plot reshaped data (matplotlib.pyplot already loaded as plt)
plt.imshow(im_sq, cmap='Greys', interpolation='nearest')
plt.show()


# Assign filename
file = 'seaslug.txt'

# Import file
data = np.loadtxt(file, delimiter='\t', dtype=str)

# Print the first element of data
print(data[0])

# Import data as floats and skip the first row
data_float = np.loadtxt(file, delimiter='\t', dtype=float, skiprows=1)

# Print the 10th element of data_float
print(data_float[9])

# Plot a scatterplot of the data
plt.scatter(data_float[:, 0], data_float[:, 1])
plt.xlabel('time (min.)')
plt.ylabel('percentage of larvae')
plt.show()


# Import file using np.genfromtxt
data = np.genfromtxt('titanic_sub.csv', delimiter=',', names=True, dtype=None)

# Print columns type
print(data.dtype)

# Print out first three entries of data
print(data[:3])

# Print column with name 'Fare'
print(data['Fare'])


# Import file using np.recfromcsv
data = np.recfromcsv('titanic_sub.csv', delimiter=',', names=True)

# Print columns type
print(data.dtype)

# Print out first three entries of data
print(data[:3])
