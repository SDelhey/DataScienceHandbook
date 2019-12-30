import numpy as np

np.random.seed(0)

# Initializing 3 random Numpy arrays of different dimensions
x1 = np.random.randint(10, size=6)
x2 = np.random.randint(10, size=(3, 4))
x3 = np.random.randint(10, size=(3, 4, 5))

print(x1)
print(x2)
print(x3)

print("---------------------")
# Indexing from behind
print(x1[-1])


print("---------------------")
# Slicing arr[start:stop:step]
print(x1[0::2])
print(x2[::2, ::-1])


print("---------------------")
# Numpy array manipulation also changes parent
slice = x2[1, :]
print(slice)
slice[0] = 23
print(slice)
print(x2)


print("---------------------")
# Copys dont manipulate the parent
copy = x2[1, :].copy()
print(copy)
copy[0] = 45
print(copy)
print(x2)

print("---------------------")
# Reshaping
reshaped = x1.reshape((6, 1))
print(reshaped)
print(x1)
