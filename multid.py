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
print(arr)
flatened_arr = arr.flatten('F') #COLUMN WISE - COLUMN MAJOR
flatened_ar2 = arr.flatten('C')#ROW WISE - ROW MAJOR

print(flatened_ar2)