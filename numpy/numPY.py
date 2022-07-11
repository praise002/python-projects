import numpy as np
"""np: numerical python
used for working with arrays
types of array: one dimensional and miulti-dimensional array
one-dimensional array: is a type of linear array e.g rank1
multi-dimensional array: stored in tabular form e.g rank 2...
axis: describes d order of indexing
e.g axis0(1 dimensional), axis1(2 dimensional), axis2(3 dimensional)
shape: d num of elements along with each axis. It is from a tuple
rank: d number of axis or dimensions it has"""

#creating list
lst1 = [1, 2, 3, 4]
#creating numpy array
sample_array = np.array(lst1)
print("List in python", lst1)
print("Numpy array in python", sample_array)
print(type(lst1))
print(type(sample_array))

#creating list
lst = [1, 2, 3, 4]
lst2 = [5, 6, 7, 8]
lst3 = [9, 10, 11, 12]
#creating numpy array
sample_array = np.array([lst,
                         lst2,
                         lst3])
print("Numpy multi-dimensional array\n", sample_array)
print("Shape of the array:", sample_array.shape)

#creating d array
sample_array_1 = np.array([[0, 4, 2]])
print(sample_array_1)
sample_array_2 = np.array([[0.2, 0.4, 2.4]])
#display data type
print("Data type of array 1:", sample_array_1.dtype)
print("Data type of array 2:", sample_array_2.dtype)

"""Ways of creating an array"""
arr = np.array([3, 4, 5, 5])
print(f"Array: {arr}")

itr = (i*i for i in range(8))
arr2 = np.fromiter(itr, float)
print("Frontier array", arr2)

var = "Geekforgeeks"
arr3 = np.fromiter(var, dtype="U2")
print("Frontier array", arr3)

#it creates a new arr of given shape and type, without initializing value
arr4 = np.empty([4, 3], dtype=np.int32, order="f")  #order can be c, f, a, k
print(arr4)

print()
arr5 = np.ones([4, 3], dtype=np.int32, order="C")
print(arr5)

print()
arr6 = np.zeros([4, 3], dtype=np.int32, order="F")
print(arr6)

