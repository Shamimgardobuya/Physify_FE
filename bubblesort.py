#!/bin/python3

import math
import os
import random
import re
import sys

def sort_with_bubble_sort(my_array):
    n = len(my_array)   
    number_swaps = 0
    #number of swaps is 0, i don't know why
    # 🐵 yes, it is because of scopes that exist 
    for i in range(n-1):
        # number_swaps = 0
        for j in range(0,n-i-1): #second iteration to start from where we left off true. inner loop only compares elements that need to be sorted
            if my_array[j] > my_array[j+1]:
                my_array[j],my_array[j+1] = my_array[j+1], my_array[j]
                number_swaps +=1            
        print(f"{number_swaps}\nfirst element is {my_array[0]}\nlast element is {my_array[-1]}")
        if(number_swaps==0):
           break
        return f"Array is sorted in {number_swaps} swaps 😉"
    
    
if __name__ == '__main__':
    # n = int(input().strip())

    # a = list(map(int, input().rstrip().split()))
    a,b,c = input().split()
    new_arr = []
    new_arr.append(int(a))
    new_arr.append(int(b))
    new_arr.append(int(c))

    
    # for i in range(new_arr):
    #     a.append(i)
    print(sort_with_bubble_sort(new_arr))
    # print(a)
    # Write your code here
