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
    
    

        
            
        
        
        
        
        
        # #!/bin/python3

# import math
# import os
# import random
# import re
# import sys
# import gc
# import itertools

# def turn_to_binary(number):
#     #input - binary o
#     #input - binary of number
#     #output - maximum number of consecutive 1's - following each other, find previous and next number
#     #
#               #how do we find the next number ina an array 1st- is [0], next  -  start + 1,f`    
#     #process- create a counter variable and assign it 0
#     #loop through the string of binary of the number
#     #if you find 1, increase counter if you find 0, return to counter to 0
#     #return final count

#        #algorithm to be bettered 
#        #check previous and after - if 
       
       
       
        
    
#     #consecutive one is do not appear on th last digit.
#     #a string of the binary of the number
#     #output - number of consecutive 1's that appear in the binary of the number
#     #process - fond the index of the elements before the last element
#     #create new string after popping the last element
#     #count the number of ones in new string
#     #return the number of consecutive ones
#       #divide string into two- check the last half- if the value of counting 1 is more than one - then subtract one and return the counting value
    
#  #identify last integer 
#     binary= bin(number)
#     count = 0
#     start = 0
#     initial = 0
#     #what happens encounter a 0 - the count will increase if next number is 1 assign 2,
#     #if next number not 1, then return count - 1
#     # for index, value in enumerate(binary):
#     #     next_number = binary[index+1]
#     #     if value == '1' and next_number == '1' and index < len(binary): 
#     #         count +=1
#     #         return count
#     #     elif value =='1' and next_number !='1' and index < len(binary):
#     #         count = 1
#     #         return count
            
            
#     new_word = iter(binary)   
#     previous = []
  

#     for next_val in itertools.takewhile(lambda x: x != 'b', binary):
        
#         #not working when trying to find output then figuring 
#         # next_val = next(new_word)
#         # th_val =   next(new_word)

#         # previous.append(binary[start])
#         # sec = len(previous) - 2
#         # third = len(previous) - 3  #want to cater for the elements after the next, up to the end of the loop because incrreamenting amount is limited to next_val, output- what if after next_val and up to the end of the list
#         if binary[start] == '1' and next_val == '1' :
#             count +=1
#             #print(previous)
#             #store in a list 
#             #count fir the third and the rest
#             #in first iteration,previous sec and previous third do not exist
#         # elif  binary[start] !='1' and previous[sec] == '1' and previous[third] == '1': #consecutive has 0, lets check previous
#             # count = int(previous[sec]) + int(previous[third])
#         elif binary[start] !='1' and next_val !='1' : 
#             count = 0
#         # elif binary[start] =='1' and next_val !='1' : 
#         #     count = 0
#             #consecutive has 0, lets check previous
        
#         #interpreter not recognizing next_index as index oof binary only start. To do, find out how to represent next number in a list in python
#         #do we know we have a fourth
#             #confirm with Conslate
#             # count = int(binary[start]) + int(next_val)
#             #getting 4 because the previous value was added and then it
#             #r
#             #less than that length of the array
#             #previous.append
#             # previous.append()
            
            
            
    
#         start += 1
#     for i in range(len(binary) - 1):
#         if binary[i] == '1' and binary[i + 1] == '1':
#             count += 1
#     return count
#      #condition fails as all binary start from digit 0 hence we jump to else condition where count has not bee increamenting - previous - element before
# #after - element aftter
# #start + 1 next
# #previous == start- 1 =0, start ==1,next 2     #find as we continue ,second iteration- start ==1 next will be 2   
#     # mid = len(binary_of_number)//2
#     # end = len(binary_of_number) - 1
#     # before = binary_of_number[0:mid]
#     # counting_start = before.count('1')
#     # after = binary_of_number[mid:end+1]
#     # counting_end = after.count('1')
#     # if len(binary_of_number) > 5: 
#     #     new_end = counting_end - 1
#     #     full_count = new_end + counting_start
#     #     print(full_count)
#     # else:
#     #     new_string = binary_of_number.replace(binary_of_number[-1],'',1)
#     #     counting = new_string.count('1') #results to a number count the 1'
#     #     print(counting)
    

#     # while mid < end:
#     #     if binary_of_number[mid] == '1':
#     #         count += 1
#     #         if count > 1:
#     #             new_count = count - 1
            
#     #     else:
#     #         continue
#     #         #print('no one found')
#     # print(counting_start + count)

#     #after - 
#     #characters before mid 
    

        
            
        
        
        
        
        
        
        
    
#     # new_string = binary_of_number.replace(binary_of_number[-1],'',1)
#     # counting = new_string.count('1') #results to a number count the 1's up to the last index- find 1's that appear before the last value 
    
    
#     # last_element = binary_of_number
#     # specific_element = [index for (index,item)in enumerate(new_list) if item == -1]
       
#     # if counting >1:
#     #     new = counting - 1
#     #     #for if count is more than 1, return for me 2 - 1 
#     #     print(new)
#     # elif counting ==1:
#     #     print(f'consecutive one is {counting},hence no consecutive')
from functools import reduce

def turn_to_binary(number):
    binary = bin(number)
    count = 0
    max_count = 0
    for c in binary:
        if c == '1':
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
    return max_count

if __name__ == '__main__':
    n = int(input().strip())
    print(turn_to_binary(n))
    

        
    
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
    







###former solutions
# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys
# import gc
# import itertools

# def turn_to_binary(number):
#     #input - binary o
#     #input - binary of number
#     #output - maximum number of consecutive 1's - following each other, find previous and next number
#     #
#               #how do we find the next number ina an array 1st- is [0], next  -  start + 1,f`    
#     #process- create a counter variable and assign it 0
#     #loop through the string of binary of the number
#     #if you find 1, increase counter if you find 0, return to counter to 0
#     #return final count

#        #algorithm to be bettered 
#        #check previous and after - if 
       
       
       
        
    
#     #consecutive one is do not appear on th last digit.
#     #a string of the binary of the number
#     #output - number of consecutive 1's that appear in the binary of the number
#     #process - fond the index of the elements before the last element
#     #create new string after popping the last element
#     #count the number of ones in new string
#     #return the number of consecutive ones
#       #divide string into two- check the last half- if the value of counting 1 is more than one - then subtract one and return the counting value
    
#  #identify last integer 
#     binary= bin(number)
#     count = 0
#     start = 0
#     initial = 0
#     #what happens encounter a 0 - the count will increase if next number is 1 assign 2,
#     #if next number not 1, then return count - 1
#     # for index, value in enumerate(binary):
#     #     next_number = binary[index+1]
#     #     if value == '1' and next_number == '1' and index < len(binary): 
#     #         count +=1
#     #         return count
#     #     elif value =='1' and next_number !='1' and index < len(binary):
#     #         count = 1
#     #         return count
            
            
#     new_word = iter(binary)   
#     previous = []
  

#     for next_val in itertools.takewhile(lambda x: x != 'b', binary):
        
#         #not working when trying to find output then figuring 
#         # next_val = next(new_word)
#         # th_val =   next(new_word)

#         # previous.append(binary[start])
#         # sec = len(previous) - 2
#         # third = len(previous) - 3  #want to cater for the elements after the next, up to the end of the loop because incrreamenting amount is limited to next_val, output- what if after next_val and up to the end of the list
#         if binary[start] == '1' and next_val == '1' :
#             count +=1
#             #print(previous)
#             #store in a list 
#             #count fir the third and the rest
#             #in first iteration,previous sec and previous third do not exist
#         # elif  binary[start] !='1' and previous[sec] == '1' and previous[third] == '1': #consecutive has 0, lets check previous
#             # count = int(previous[sec]) + int(previous[third])
#         elif binary[start] !='1' and next_val !='1' : 
#             count = 0
#         # elif binary[start] =='1' and next_val !='1' : 
#         #     count = 0
#             #consecutive has 0, lets check previous
        
#         #interpreter not recognizing next_index as index oof binary only start. To do, find out how to represent next number in a list in python
#         #do we know we have a fourth
#             #confirm with Conslate
#             # count = int(binary[start]) + int(next_val)
#             #getting 4 because the previous value was added and then it
#             #r
#             #less than that length of the array
#             #previous.append
#             # previous.append()
            
            
            
    
#         start += 1
#     for i in range(len(binary) - 1):
#         if binary[i] == '1' and binary[i + 1] == '1':
#             count += 1
#     return count
#      #condition fails as all binary start from digit 0 hence we jump to else condition where count has not bee increamenting - previous - element before
# #after - element aftter
# #start + 1 next
# #previous == start- 1 =0, start ==1,next 2     #find as we continue ,second iteration- start ==1 next will be 2   
#     # mid = len(binary_of_number)//2
#     # end = len(binary_of_number) - 1
#     # before = binary_of_number[0:mid]
#     # counting_start = before.count('1')
#     # after = binary_of_number[mid:end+1]
#     # counting_end = after.count('1')
#     # if len(binary_of_number) > 5: 
#     #     new_end = counting_end - 1
#     #     full_count = new_end + counting_start
#     #     print(full_count)
#     # else:
#     #     new_string = binary_of_number.replace(binary_of_number[-1],'',1)
#     #     counting = new_string.count('1') #results to a number count the 1'
#     #     print(counting)
    

#     # while mid < end:
#     #     if binary_of_number[mid] == '1':
#     #         count += 1
#     #         if count > 1:
#     #             new_count = count - 1
            
#     #     else:
#     #         continue
#     #         #print('no one found')
#     # print(counting_start + count)

#     #after - 
#     #characters before mid 
    

        
            
        
        
        
        
        
        
        
    
#     # new_string = binary_of_number.replace(binary_of_number[-1],'',1)
#     # counting = new_string.count('1') #results to a number count the 1's up to the last index- find 1's that appear before the last value 
    
    
#     # last_element = binary_of_number
#     # specific_element = [index for (index,item)in enumerate(new_list) if item == -1]
       
#     # if counting >1:
#     #     new = counting - 1
#     #     #for if count is more than 1, return for me 2 - 1 
#     #     print(new)
#     # elif counting ==1:
#     #     print(f'consecutive one is {counting},hence no consecutive')
from functools import reduce

def turn_to_binary(number):
    binary = bin(number)
    count = 0
    max_count = 0
    for c in binary:
        if c == '1':
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
    return max_count

if __name__ == '__main__':
    n = int(input().strip())
    print(turn_to_binary(n))
    
