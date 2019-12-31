import numpy as np

arr = np.arange(1, 10)

# Saving into variable
print(arr)
np.multiply(arr, 2, out=arr)
print(arr)


print("-----------------")
# Aggregation
print(np.add.reduce(arr))
print(np.multiply.reduce(arr))
print(np.multiply.accumulate(arr))


print("-----------------")
#  Boolean operators
print(arr)
print(arr > 15)

print("-----------------")
# Masking
print(arr)
mask = arr[arr > 15]
mask[0] = 100
print(mask)
print(arr)


print("-----------------")
x = np.random.randn(100)
bins = np.linspace(-5, 5, 20)
counts = np.zeros_like(bins)
print(x)
print(bins)
print(counts)
i = np.searchsorted(bins, x)
print(i)
