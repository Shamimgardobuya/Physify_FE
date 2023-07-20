#________________Adding elements to a multdimensional array
#pseudocode

#create a 2d array in Python
#create another 2d array
#using the + operator add the 2d arrays
  #adding a different dimension e⬇️ 
     #⛔   
        #ValueError: operands could not be broadcast together with shapes (2,3) (1,2,5) 
# Write a program to insert the element into the 2D (two dimensional) array of Python. from array import * # import all package related to the array.
#It's a numpy library , we can use multiplication provided.



#removing element from an mmultidimensional array using indexing, there's value then there's by index 
#pseudocode

#
import numpy as np
arr = np.array([[1,2,3],[124,34,12]])
second_arr = np.array([[0,3,3],[0,1,1]]) 
third_arr = np.array([[[1,2,3,4,5],[5,4,5,3,2]]])
#slice the array 🤠 using indexing 
# array_name[start_index_row:end_index_row,start_index_column:end_index_column]

sliced_arr = arr[1:2] #slicing is per row, row wise 
#acessing a range of values, 
# I want  a sub-array containing 124 and 34 
sliced_arr_two = arr[1:,0:2]
print(sliced_arr_two)

# print(arr)
# print(sliced_arr)
# print(np.shape(arr)) #output ↪️ (2,3) shape of the multidimensional array -  rows first index, columns second
# print(arr + third_arr) 
# for i in arr:
    # for i in arr:
    #     for i in arr:
    #         for i in arr:
    #             for i in arr:
    #                 print(i)


# arr4 = np.insert([1,2]
# print(len(arr))
#axis 1 -represents 1st column, axis 0, represents row1
arr4 = np.delete(arr,[0][0],1) #takes 3 args, 1,name of array, 2, argument index, a must, 3rd argument-axis   
# print(arr4)
# arr_second = np.delete(arr, [1, 2] ,1) #takes 3 args, 1,name of array, 2, argument index, a must, 3rd argument-axis   
arr_second = np.delete(arr, 1 ,1) #takes 3 args, 1,name of array, 2, argument index, a must, 3rd argument-axis    
#e ➡️ removes middle column 
# print(arr_second)
#removing elements from a row.
#use axis 0
# to remove a particular row using from the array 
arr_remove_row = np.delete(arr,0,axis=0) #⤵
# print(arr_remove_row)
#each value is mapped according to their positions then added 
# print(arr)

#how to remove an element in an array 
#pseudocode
#using delete and where 
arr3= np.delete(arr,np.where(arr==34))
# print(arr3)
#flattening an array - row wise - C
#flattening column wise - Fortran
# 
# print(arr)
arr2 = np.array([[ 1.07, 0.44 , 1.5  , 0.2  , 3.2 , 1.18 , 0.09 , 1.44  ,1.52 , 2.44,  0.78 , 0.02]
 [ 0.27,  1.13 , 1.72,  4.14 , 2.66 , 0.61 , 1.03 , 1.4 , 18.16 , 2.24 , 0.29,  0.5 ]])
flatened_arr = arr2.flatten('F') #COLUMN WISE - COLUMN MAJOR
flatened_ar2 = arr.flatten('C')#ROW WISE - ROW MAJOR

print(flatened_arr)