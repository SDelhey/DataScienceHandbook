import numpy as np

# UFuncs are vectorized operations
# UFuncs are way faster because they can be executed inside the compiled Numpy layer
# No type checking for every element necessary

# Standard UFunc
arr = np.random.randint(1, 5, 5)
print(arr)
print(arr ** 2)


print("-----------------------")
# Trigonometrics
print(arr)
print(np.sin(arr))
print(np.cos(arr))
print(np.arctan(arr))


print("-----------------------")
# Exponents and Logarithms
print(arr)
print(np.exp(arr))
print(np.power(arr, 3))
print(np.log(arr))