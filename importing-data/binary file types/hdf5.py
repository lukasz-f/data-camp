import numpy as np
import matplotlib.pyplot as plt
import h5py

# Assign filename
file = 'LIGO_data.hdf5'

# Load file
data = h5py.File(file, 'r')

# Print the datatype of the loaded file
print(type(data))

# Print the keys of the file
for key in data.keys():
    print(key)

# Print the datatype of meta-data
print(type(data['meta']))

# Print the keys of meta-data
for key in data['meta'].keys():
    print(key)

# Print the meta-data value
print(data['meta']['Description'].value)

# Get the HDF5 group
group = data['strain']

# Check out keys of group
for key in group.keys():
    print(key)


# Set variable equal to time series data
strain = data['strain']['Strain'].value

# Set number of time points to sample
num_samples = 10000

# Set time vector
time = np.arange(0, 1, 1/num_samples)

# Plot data
plt.plot(time, strain[:num_samples])
plt.xlabel('GPS Time (s)')
plt.ylabel('strain')
plt.show()
