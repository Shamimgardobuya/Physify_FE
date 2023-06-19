#!/bin/python3

import math
import os
import random
import re
import sys

def reverse_list(my_list):
    
    print(my_list)
    first = 0
    last = len(my_list) - 1
    while first < last:   #using 2 pointer approach
         temporary_store = my_list[first]
         my_list[first] = my_list[last]
         my_list[last] = temporary_store
         last -= 1
         first += 1
        #  start +=1
    print(my_list)
    
   #if white spaces exist in between values of the list.
# reverse_list([6676 3216 4063 8373 423 586 8850 6762])

if __name__ == '__main__':
    n = int(input().strip())# removes whitespaces
    for i in range(0,n):    #rstrip removes the last whitespaces that are present on the end of the list
       arr = list(map(int, input().rstrip().split()))  # whitespaces can still be considered to be split because no other delimeter is present
       delimeter = [',' , ';', ' ']
       for symbol in delimeter:
        if symbol in arr:      
            reverse_list(arr)
        # loop through to get the values added in the list 
    #Input- a size of an array. Then an array. Output, the array of the size mentioned in reverse form.
    # Process - create a function that accepts the array, using slicing reverse the list using for loop
    
    
