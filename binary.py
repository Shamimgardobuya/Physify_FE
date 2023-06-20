from audioop import reverse
import math
import os
import random
import re
import sys
import string

# letters = list(string.ascii_lowercase)  #want to check if it is right base 
base_ten = [0,1,2,3,4,5,6,7,8,9]
def turn_to_binary(number):
    if number == 0:    #base case not seem to find one 
        return 0
    if number not  in base_ten:
        # print(number)

        return number
    # elif number == 1 :
    #     return
    else:
        new_list = []
        quotient = number//2
        if quotient != 0:
          new_list.append(turn_to_binary(quotient%2))
        return new_list
    

if __name__ == '__main__':
    print(turn_to_binary(3))
       #capture for me the value, wh
        # new_list.append(bin2) 
        # x = new_list.reverse()
        # else:
        #     new_list.append(bin2)
        
    
    #     return new_list
    #input - number
    #output - number in binary form
    # process - need quotient and remainder -
    #reverse the remainders order
    #create a function
    #find qoutents of all the numbers of that number 
    #find the modulus of each of the quotients with 2
    #append the numbers to a list
    #reverse the list and print the content of the list
    #that will be the binary
    #orig/2 - continue until result  = = 0

    # new_list = []
    # quotient = number//2
    # bin2 = number %2
    # while quotient!=0:
    #     rems = quotient%2
    #     new_list.append(rems)
    # print(new_list)