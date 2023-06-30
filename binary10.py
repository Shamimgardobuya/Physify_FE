#!/bin/python3

import math
import os
import random
import re
import sys
import gc


def turn_to_binary(number):
    #consecutive one is do not appear on th last digit.
    #a string of the binary of the number
    #output - number of consecutive 1's that appear in the binary of the number
    #process - fond the index of the elements before the last element
    #create new string after popping the last element
    #count the number of ones in new string
    #return the number of consecutive ones
      #divide string into two- check the last half- if the value of counting 1 is more than one - then subtract one and return the counting value
    
    binary_of_number = bin(number)
    mid = len(binary_of_number)//2
    before = binary_of_number[0:mid]
    counting_start = before.count('1')
    
    end = len(binary_of_number) - 1
    count = 0
    while mid < end:
        if binary_of_number[mid] == '1':
            count += 1
        else:
            continue
    if count > 1:
        new_count = count - 1   
    print(counting_start + new_count)

    #after - 
    #characters before mid 
    
    

        
            
        
        
        
        
        
        
        
    
    # new_string = binary_of_number.replace(binary_of_number[-1],'',1)
    # counting = new_string.count('1') #results to a number count the 1's up to the last index- find 1's that appear before the last value 
    
    
    # last_element = binary_of_number
    # specific_element = [index for (index,item)in enumerate(new_list) if item == -1]
    
    # if counting >1:
    #     new = counting - 1
    #     #for if count is more than 1, return for me 2 - 1 
    #     print(new)
    # elif counting ==1:
    #     print(f'consecutive one is {counting},hence no consecutive')

if __name__ == '__main__':
    n = int(input().strip())
    turn_to_binary(n)
    


