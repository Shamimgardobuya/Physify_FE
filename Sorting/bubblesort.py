# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# def sort_with_bubble_sort(my_array):
#     n = len(my_array)   
#     number_swaps = 0
#     #number of swaps is 0, i don't know why
#     # 🐵 yes, it is because of scopes that exist 
#     for i in range(n-1):
#         # number_swaps = 0
#         for j in range(0,n-i-1): #second iteration to start from where we left off true. inner loop only compares elements that need to be sorted
#             if my_array[j] > my_array[j+1]:
#                 my_array[j],my_array[j+1] = my_array[j+1], my_array[j]
#                 number_swaps +=1            
#         print(f"{number_swaps}\nfirst element is {my_array[0]}\nlast element is {my_array[-1]}")
#         if(number_swaps==0):
#            break
#         return f"Array is sorted in {number_swaps} swaps 😉"
    
    
# if __name__ == '__main__':
#     # n = int(input().strip())

#     # a = list(map(int, input().rstrip().split()))
#     a,b,c = input().split()
#     new_arr = []
#     new_arr.append(int(a))
#     new_arr.append(int(b))
#     new_arr.append(int(c))

    
#     # for i in range(new_arr):
#     #     a.append(i)
#     print(sort_with_bubble_sort(new_arr))
#     # print(a)
#     # Write your code here
def bubble_sort(arr):
    # Get the length of the array
    arr_len = len(arr)
    # Loop through the array to access the elements in it, including the last one - outer loop
    for i in range(arr_len-1):
        # declare a flag variable to check if a swap has occured - for optimization
        # flag = 0
        # create a loop to compare each element of the array till the last one
        for j in range(0, arr_len-i-1):
            flag = 0
            # compare 2 adjacent elements and sort them in ascending order
            if arr[j] > arr[j+1]:
                # Swap the elements if they are not in the right order
                arr[j+1], arr[j] = arr[j], arr[j+1]
                flag = 1
                # break out of the loop at 0
                if flag == 0:
                    break
    # return value must be in the outer loop block
            return  flag

arr = [5, 3, 4, 1, 2]
#3, 4,1,2 5
#3, 1, 2, 4, 5
#1,2,3,4,5
print(bubble_sort(arr))