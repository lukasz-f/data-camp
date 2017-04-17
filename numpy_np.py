import numpy as np

# NumPy arrays creation
np_numbers = np.array([1, 2, 3, 4, 5, 6])
type(np_numbers)  # <class 'numpy.ndarray'>

# 2D NumPy array creation
np_numbers2d = np.array([[1, 2, 3], [11, 22, 33]])

# NumPy arrays info
np_numbers.ndim  # ilosc wymiarow = 1
np_numbers2d.ndim  # 2
np_numbers.shape  # rozmiar = (6,)
np_numbers2d.shape  # (2, 3)
np_numbers.size  # ilosc elementow = 6
np_numbers2d.size  # 6

np_numbers.dtype  # int64

# Changes NumPy arrays dimensions
np_numbers.reshape(2, 3)  # array([[1, 2, 3], [4, 5, 6]])
np_numbers.shape = (2, 3)  # array([[1, 2, 3], [4, 5, 6]])
np_numbers.shape = (-1, 2)  # -1 = calculate dimension
np_numbers.shape = (3, 2, 1)  # array([[[1], [2]], [[3], [4]], [[5], [6]]])
np_numbers.flatten()  # array([1, 2, 3, 4, 5, 6])
np_numbers.ravel()  # array([1, 2, 3, 4, 5, 6])
# flatten returns a copy
# ravel returns a view of the original array

# NumPy array arithmetic operations
np_numbers + np_numbers  # array([2, 4, 6, 8, 10, 12])
np_numbers * 0.2  # array([0.2, 0.4, 0.6, 0.8, 1., 1.2])
np_numbers2d + 1  # array([[2, 3, 4], [12, 23, 34]])
np_numbers2d + np.array([3, 2, 1])  # array([[4, 4, 4], [14, 24, 34]])
np_numbers2d * 2  # array([[2, 4, 6], [22, 44, 66]])
np_numbers2d * np.array([1, 0.5, 2])  # array([[1., 1., 6.], [11., 11., 66.]])

# boolean NumPy array
np_numbers > 3  # array([False, False, False, True, True], dtype=bool)
np.array([1,7,9]) <= np.array([4,5,6])  # array([True, False, False], dtype=bool)
1 != np.eye(3, 3)  # array([[False, True, True], [True, False, True], [True, True, False]], dtype=bool)
(np_numbers > 3) & (np_numbers <= 5)  # array([False, False, False, True, True, False], dtype=bool)
np.all((np_numbers > 3) | (np_numbers <= 5))  # True
np.any((np_numbers > 3) & (np_numbers <= 5))  # True

# Subsetting
np_numbers[0]  # 1
np_numbers[:3]  # array([1, 2, 3])
np_numbers[np_numbers > 3]  # array([4, 5])
np_numbers2d[(np_numbers2d > 2) & (np_numbers2d < 22)] = 99  # array([[1, 2, 99], [99, 22, 33]])

# Type coercion
np.array([True, 1, 2])  # array([1, 1, 2])
np.array([3, 4, False])  # array([3, 4, 0])
np.array([1.0, 'is', True])  # array(['1.0', 'is', 'True'], dtype='<U32')

# Join NumPy Arrays
# Concatenates along the first axis
np.vstack((np_numbers2d, [97, 98, 99]))  # array([[1, 2, 3], [11, 22, 33], [97, 98, 99]])
np.concatenate((np_numbers2d, [[97, 98, 99]]), axis=0)
np.r_[np_numbers2d, [[97, 98, 99]]]
np.c_['0', np_numbers2d, [[97, 98, 99]]]
np.insert(np_numbers2d, 1, [[97, 98, 99]], axis=0)  # array([[1, 2, 3], [97, 98, 99], [11, 22, 33]])
# Concatenates along the second axis
np.hstack((np_numbers2d, [[98], [99]]))  # array([[1, 2, 3, 98], [11, 22, 33, 99]])
np.concatenate((np_numbers2d, [[98], [99]]), axis=1)
np.c_[np_numbers2d, [[98], [99]]]
np.r_['1', np_numbers2d, [[98], [99]]]
np.insert(np_numbers2d, 1, [[98,99]], axis=1)  # array([[1, 98, 2, 3], [11, 99, 22, 33]])

np.r_[np.array([1, 2, 3]), 0, 0, [4, 5, 6]]  # array([1, 2, 3, 0, 0, 4, 5, 6])
np.c_[1:6:3j, [7, 8, 9]]  # array([[1., 7.], [3.5, 8.], [6., 9.]])

# 2D Numpy array subsetting
np_numbers2d[1]  # array([11, 22, 33])
np_numbers2d[1,]  # array([11, 22, 33])
np_numbers2d[1,:]  # array([11, 22, 33])
np_numbers2d[1][2]  # 33
np_numbers2d[1, 2]  # 33
np_numbers2d[:, 2]  # array([3, 33])

# Statistics
np.mean(np_numbers)  # 3 (średnia arytmetyczna, average)
np.median(np_numbers)  # 3 (mediana, median)
np.corrcoef(np_numbers2d[0], np_numbers2d[1])  # array([[1., 1.],[1., 1.]]) # (korelacja, correlation)
np.std(np_numbers)  # 1.4142135623730951 (odchylenie standardowe, standard deviation)

# Generate data
# Rozklad jednostajny, wszystkie wartosci z przedzialu sa jednakowo prawdopodobne, wykres jako prostokat
np.random.uniform(-4, 4, 5)  # array([-0.67943812, 1.1968127, 3.95681398, -0.11253058, 0.03629631])

# Rozklad normalny, wartosc oczekiwana i odchylenie standardowe
np.random.normal(-4, 4, 5)  # array([-0.17356846, -2.11547504, 3.3831675, -2.57351, -2.90367374])

height = np.round(np.random.normal(1.75, 0.20, 5000), 2)
weight = np.round(np.random.normal(60.32, 15, 5000), 2)
np_city = np.column_stack((height, weight))

np.random.randint(2, 5)  # generuj liczbe z przedzialu
np.random.randint(2, 5, 10)  # generuj 10 liczb z przedzialu

# List generator
np.arange(5)  # array([0, 1, 2, 3, 4])
np.arange(2, 8)  # array([2, 3, 4, 5, 6, 7])
np.arange(2, 8, 2)  # array([2, 4, 6])
np.arange(start=2, stop=8, dtype=np.float64)  # array([2., 3., 4., 5., 6., 7.])

np.linspace(0, 1, 5)  # array([0., 0.25, 0.5, 0.75, 1.])
np.linspace(0, 1, 5, endpoint=False)  # array([0., 0.2, 0.4, 0.6, 0.8])

np.r_[2:8]  # array([2, 3, 4, 5, 6, 7])
np.r_[2:8:2]  # array([2, 4, 6])
np.r_[0:1:5j]  # array([0., 0.25, 0.5, 0.75, 1.])

np.c_[2:8] # array([[2], [3], [4], [5], [6], [7]])
np.c_[0:1:5j]  # array([[0.], [0.25], [0.5], [0.75], [1.]])

np.random.choice(np.arange(10), 3, replace=False)  # losuj 3 liczby bez powtorzen z przedziału [0-9]
np.random.choice([4, 6, 8], 30, replace=True)  # losuj 30 liczb z powtorzeniami z listy [4, 6, 8]
np.random.choice(["asd", "dsa", "qqq"], 11, replace=True)  # losowanie stringow
np.repeat(5, 6)  # array([5, 5, 5, 5, 5, 5])
np.repeat([1, 2], 3)  # array([1, 1, 1, 2, 2, 2])
np.tile(5, 6)  # array([5, 5, 5, 5, 5, 5])
np.tile([1, 2], 3)  # array([1, 2, 1, 2, 1, 2])

# Array generator
np.eye(5)  # macierz jednostkowa 5x5 (jedynki na przekątnej)
np.eye(4, 5)  # macierz jednostkowa niekwadratowa 4x5
np.diag([1, 2, 3])  # macierz diagonalna 3x3 (podane wartości na przekątnej)
np.zeros((3, 5))  # macierz zerowa 3x5 (same zera w macierzy)
np.ones((3, 5))  # macierz samych jedynek 3x5
np.empty((2, 3))  # pusta macierz z losowymi wartosciami

# W NumPy slicing nie robi kopi w przeciwienstwie do pythona
x = np.r_[1,2,3]
y = x[0:2]
y[0] = 100  # modyfikuje liste x i y

np_numbers2d.sum()  # suma wszystkich elementów
np_numbers2d.sum(axis=0)  # array([12, 24, 36])
np_numbers2d.sum(axis=1)  # array([ 6, 66])
np.sum(np_numbers > 2)  # 4
np.sum(np_numbers[np_numbers > 2])  # 18
np.sort(np.random.randint(2, 5, 10))  # array([2, 2, 2, 2, 2, 3, 3, 4, 4, 4])
np.sort(np.array([[3,2,5],[1,6,4],[8,7,9]]), axis=0)  # array([[1, 2, 4], [3, 6, 5], [8, 7, 9]])
np.sort(np.array([[3,2,5],[1,6,4],[8,7,9]]), axis=1)  # array([[2, 3, 5], [1, 4, 6], [7, 8, 9]])
np.minimum([2, 3, 4], [1, 5, 2])  # array([1, 3, 2])
np.apply_along_axis(np.mean, 0, np_numbers2d)  # array([6., 12., 18.])
np.apply_along_axis(np.mean, 1, np_numbers2d)  # array([2., 22.])
np.unique(np.array([1, 3, 1, 2, 4, 1, 2, 3]))  # array([1, 2, 3, 4])
