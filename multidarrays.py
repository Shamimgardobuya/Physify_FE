import numpy as np
# arr = np.array([[1,2,3,5],[4,5,6,7],[34,367,67,23]])
arr2 = [[1,2,3,4],[1,2,4,5]]
# print(type(arr),type(arr2))
# print(arr)
#access element 5
#row 0,3
# print(arr[0,3])

#create a 3d array and find a paricular element using indexing
array_third = np.array([[[1,2,3,4,5],[1,2,53,1,5]], 
                        #0
                         [[3,4,5,6,7],[12,34,5,6,7]],
                         [[12,34,56,67,57],[90,45,45,59,44]]
                         ])
 #1
 #Error received when creating different lengths for the columns
 #VisibleDeprecationWarning: Creating an ndarray from ragged nested sequences (which is a list-or-tuple of lists-or-tuples-or ndarrays with different lengths or shapes) is deprecated. If you meant to do this, you must specify 'dtype=object' when creating the ndarray.
 #have to work with same number of columns different number of columns for each row is no longer being used.
# print(array_third[0][1][2]) #53 remember row and column, they are nested but still use indexing
# print(array_third[1][1][1]) #34
#53
#4D array an array of 3D Arrays
# 3d arrays a cube - 2d arrays 3 times  
#task
#create a 4D array
#After creating a 4d array access an element through indexing, find 89,78

array_four = np.array([
                       [[[1,2],[3,4],[5,6]]],
                       [[[12,23],[78,34],[56,39]]],
                       [[[11,23],[45,21],[89,65]]]
                       ])
# print(array_four)
#error initially when using print(array_four[2][2][0])-  index error index 1 is out of bounds for axis 0 with size 1- meaning the size of the array is less 1 so 0 - playing with indexing is fun
# print(array_four[2][0][2][0])#89
# print(array_four[1][0][1][0])  #78

# for i in array_four:
#     print(i)


#

#using arr,
# Access a subarray that contains rows 0 through 1 and columns 1 through 2
arr = np.array([[1,2,3,5],[4,5,6,7],[34,367,67,23]])
subarr = arr[0:2,1:3]
subarr*=2
print(subarr) #yaay it has multiplied each value of subarr without looping
#find sum of sub arr
print(np.sum(subarr))
#calculate mean of each row- function works with flattened array
print(np.mean(subarr, axis=1))  # Output: [ 2.5  6.5 10.5]
# print(np.mean())
# Calculate the dot product of two matrices  - multiplication of two matrices - row by column , nb - row and column have to be of equal length

