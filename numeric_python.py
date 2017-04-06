import numpy as np

# Numpy arrays creation
np_numbers = np.array([1, 2, 3, 4, 5])
type(np_numbers)  # <class 'numpy.ndarray'>

# Numpy array arithmetic operations
np_numbers + np_numbers  # array([ 2,  4,  6,  8, 10])
np_numbers * 0.2  # array([ 0.2,  0.4,  0.6,  0.8,  1. ])

# boolean Numpy array
np_numbers > 3  # array([False, False, False, True, True], dtype=bool)

# Subsetting
np_numbers[0]  # 1
np_numbers[:3]  # array([1, 2, 3])
np_numbers[np_numbers > 3]  # array([4, 5])

# Type coercion
np.array([True, 1, 2])  # array([1, 1, 2])
np.array([3, 4, False])  # array([3, 4, 0])
np.array([1.0, 'is', True])  # array(['1.0', 'is', 'True'], dtype='<U32')

# 2D Numpy array creation
np_numbers2d = np.array([[1, 2, 3], [11, 22, 33]])

# Check array dimension
np_numbers2d.shape  # (2, 3)

# 2D Numpy array subsetting
np_numbers2d[1]  # array([11, 22, 33])
np_numbers2d[1,]  # array([11, 22, 33])
np_numbers2d[1,:]  # array([11, 22, 33])
np_numbers2d[1][2]  # 33
np_numbers2d[1, 2]  # 33
np_numbers2d[:, 2]  # array([3, 33])

np_numbers2d + 1  # array([[2, 3, 4], [12, 23, 34]])
np_numbers2d + np.array([3, 2, 1])  # array([[4, 4, 4], [14, 24, 34]])
np_numbers2d * 2  # array([[2, 4, 6], [22, 44, 66]])
np_numbers2d * np.array([1, 0.5, 2])  # array([[1., 1., 6.], [11., 11., 66.]])

# Statistics
np.mean(np_numbers)  # 3 (średnia arytmetyczna, average)
np.median(np_numbers)  # 3 (mediana, median)
np.corrcoef(np_numbers2d[0], np_numbers2d[1])  # array([[1., 1.],[1., 1.]]) # (korelacja, correlation)
np.std(np_numbers)  # 1.4142135623730951 (odchylenie standardowe, standard deviation)
np.sum
np.sort

# Generate data
height = np.round(np.random.normal(1.75, 0.20, 5000), 2)
weight = np.round(np.random.normal(60.32, 15, 5000), 2)
np_city = np.column_stack((height, weight))
