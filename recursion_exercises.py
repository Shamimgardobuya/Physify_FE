#  Write a recursive function 
# that accepts two numbers 
# as its argument and returns its power
#first argument, number then second number is for the power of the number
#subtask,is - 
#what if its 8,8, 8,7 86, 85, 84,83,82,81
#n^n-1
#if numb == 0
#FIND BASE CASE #if numb == 0
#create function power
#inside parameters,
#create param name n
#creaet a base case
#repeated subtask(n^n-1)
#NUMB 
#power decreasing
#subtask is 8*7,
#number get the power, repeating will be number^4,number
#
#Write a program that reads two integers from 
#keyboard and calculate the greatest common 
#divisor (gcd) using recursive function
#base number - number
#exponent the power - in python **
def find_power(number):
    if number == 0:
        return number
    else:
        # print(find_power(number**number - 1))
        return number ** find_power(number - 1)
   

for i in range(0,4):
    print(find_power(i))
#0,1,2,9,
#first call number is 
#  3**2 power is 2

# 9
# >>> 2**1 second call number is 2 , power is now 1
# 2
# >>> 1**0 third call number is 1, power is now 0
# 1
# >>> 0**0 fourth call number is 0, power is now 
# 0


