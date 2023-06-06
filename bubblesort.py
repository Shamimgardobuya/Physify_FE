#!/bin/python3

import math
import os
import random
import re
import sys

def sort_with_bubble_sort(array):
    number_swaps = 0
    n = len(array) 
    for i in range(n):
        print(array)
        for j in range(0,n-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1], array[j]
                number_swaps +=1
        statement = f"Array is sorted in {number_swaps}swaps."
        first = f"First Element : {array[0]}"
        last = f"Last Element: {array[-1]}"
        print(f"""{statement}
            {first}
            {last}
            """)
        if(number_swaps==0):
           break
        print("Array is sorted in 0 swaps.")
    
    
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))
    for i in range(n):
        a.append(i)
    sort_with_bubble_sort(a)
    # print(a)
    # Write your code here
