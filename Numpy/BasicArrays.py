import numpy as np

# Creating a basic Numpy array
arr = np.array([1, 2, 3, 4])
print(arr)

# Creating a Numpy array with 0
zeros = np.zeros(10)
print(zeros)


# Creating a Numpy array with 1
ones = np.ones(5)
print(ones)

# Create a Numpy array with 4 elements evenly distributed between 1 and 2
lin = np.linspace(1, 2, 4)
print(lin)

# Create a Numpy array from a normal distribution with mean 0 sd 1 and size 1x4
normal = np.random.normal(0, 1, 4)
print(normal)
