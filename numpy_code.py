import numpy as np

# arr = np.array([1, 2, 3, 4, 5])
# print(arr)

# sum = arr[1] + arr[2]
# print(sum)

# arr = np.array([[1,2,3,4,5],[6,7,8,9,0]])
# print(arr[0,1])

# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# print(arr)

# arr = np.array([1, 2, 3, 4, 5, 6, 7])
# print(arr[:4])
# print(arr[1:5:2])
# print(arr[::2])
# print(arr.dtype)


# arr = np.array(['apple', 'banana', 'cherry'])
# print(arr.dtype)

# arr = np.array([1, 2, 3, 4], dtype='S')
# print(arr)
# print(arr.dtype)


# arr = np.array([1, 2, 3, 4], dtype='i4')
# print(arr)
# print(arr.dtype)

# arr = np.array([1, 2, 3, 4, 5])
# print(arr)
# x = arr.copy()
# arr[0] = 44
# print(x)
# print(arr)

# arr = np.array([1, 2, 3, 4, 5])
# x = arr.view()
# arr[0] = 42
# print(arr)
# print(x)

# arr = np.array([1, 2, 3, 4, 5])
# x = arr.copy()
# y = arr.view()
# print(x.base)
# print(y.base)

# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# arr = np.array([1, 2, 3, 4], ndmin=5)
# print(arr.shape)

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# new_arr = arr.reshape(4,3)
# print(new_arr)

# arr = np.array([1, 2, 3])
# for x in arr:
#   print(x)

# arr = np.array([[1, 2, 3], [4, 5, 6]])
# for x in arr:
#   print(x)

# arr = np.array([[1, 2, 3], [4, 5, 6]])
# for x in arr:
#   for y in x:
#     print(y)

# arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# for x in np.nditer(arr):
#   print(x)

# arr1 = np.array([[1, 2], [3, 4]])
# arr2 = np.array([[5, 6], [7, 8]])
# arr = np.concatenate((arr1, arr2))
# print(arr)

# arr = np.array([True, False, True])
# print(np.sort(arr))

from numpy import random
x = random.randint(1000 ,9999)
print(x)
