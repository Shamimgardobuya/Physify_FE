from audioop import reverse
import math
import os
import random
import re
import sys
import string
from itertools import chain
# letters = list(string.ascii_lowercase)  #want to check if it is right base 
base_ten = [0,1,2,3,45,6,7,8,9]
def turn_to_binary(number):
     new_list =[]
     #if number == 0:
      #return 0
     if number < 2:
      return 0
     elif number % 2 == 0 or number %2 != 0 or number %2 < 0:  #until quotient = = 0 - include the 0
      return [turn_to_binary(number // 2)] + [number // 2]
     else:
      return []
  #if number == 0:    #base case not seem to find one 
       # return 0
   # if number not  in base_ten:
       # return number
    # elif number == 1 :
    #     return
   # else:
        #new_list = []
        #quotient = number//2
        #if quotient != 0:   
          #return  turn_to_binary(quotient//2)
       # else:
         #return quotient'''
    
#until quotient is 0
#if __name__ == '__main__':
   #print(turn_to_binary(3))
    
'''from audioop import reverse
import math
import os
import random
import re
import sys
import string

# letters = list(string.ascii_lowercase)  #want to check if it is right base 
base_ten = [0,1,2,3,4,5,6,7,8,9]
#find repeated subtraction is - 5 many times, but also this one results to the start value
#tell computer , each step is divisible by i is not defined - i could be 9, 
def turn_to_binary(number):
    #the first iteration ; it depends with the value - value am giving - if it is at 7 - we will need the quotient to to only hold from the number of iterations until quotient ends at 0
    quotient_array = []
    #number is not a range, fn
    a = number //2
    b = a//2
    c = b//2
    d = c//2
    #ALGORITHM NEEDED, NOT YET THERE- WHAT ARE MY QUOTIENTS - QUOTIENTS - NOT YET THERE- TELL THE MACHONE WHAT TO DO, manually  i can't get the numbers of quotients- but even the step is a bit tricky, 9//2,i//2,i//2,ii/2
  
    return f"{b} {quotient_array}"
    #find quotient  first then you can get binary 
   # for i in (number,1):  #getting 0 as 
    #  c = b//2
      #a = b
     # b = c
      #d = b
     # e = d
    #return f"{b} {quotient_array}"
        #quotient_array.append(b)
        #resulting is 0, tell software to move a step- repeated subtrctioon

    
        
    # if number == 0:    #base case not seem to find one 
    #     return 0
    # # if number not  in base_ten:
    # #     # print(number)

    # #     return number
    # # # elif number == 1 :
    # # #     return
    # else:
    #     new_list = []
    #     quotient = number//2
    #     if quotient != 0:
    #           new_list.append(turn_to_binary(quotient%2))
    #           return new_list
    #     else:
    #         return quotient
            #we ould like to save the data of the quotients  then actually come up with something better and goof
    
#find array of qutients
#create a function that takes in a number then
#creae an empty array- how many times will 2 get into the number - unknown, we have starting point
#'''
#from operator import add

if __name__ == '__main__':
   #z= turn_to_binary(87)
   #print(z)
   '''new = []
   new.append(z)
   #print(new)
   p = list(chain.from_iterable(new))
   p= reduce(add,z)
   for i in p:
    print(i)
   print(len(p))'''

   
      #origin = turn_to_binary(87)[0][0][0][0]
   origin =1
   item_one = turn_to_binary(27)[0][0][0][1]
   item_two = turn_to_binary(27)[0][0][1]
   item_three = turn_to_binary(27)[0][1]
   second_last = turn_to_binary(27)[1]
   last = 27
   #print(origin)
   rem = last-(second_last*2)
   rem2 = second_last-(item_three*2)
   rem3 = item_three -(item_two *2)
   rem4 = item_two -(item_one*2)
   rem5 = item_one - (origin*2)
   new_list = []
   new_list.append(rem5)
   new_list.append(rem4)
   new_list.append(rem3)   
   new_list.append(rem2)   
   new_list.append(rem)
   specific_element = [index for (index,item)in enumerate(new_list) if item == -1]
   new_list[specific_element[0]] = 1
   print(new_list)
   '''reverse = []
   for i in new_list:
    
    reverse.append(i%2)
   print(reverse[::-1])'''
   '''for i in range(19):
        pass
    print(turn_to_binary(i))'''
    
  # print(turn_to_binary(17))
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
    
    #iteration is 4 times, create variable for holding the 4 digits , append in another array then loop through,find modulus of each with 2 
  
