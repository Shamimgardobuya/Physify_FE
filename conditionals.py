#!/bin/python3

import math
import os
import random
import re
import sys

#create an input argument and check the input value
#create a funciton and pass in a value as parameter
#inside the function block
#check if n is odd, if odd print "weird"
#if n is even and part of range 2 to 5 print "not weird"
#if even and part of range 6 to 20, print Weird
#if n is greater than 20 print not wweird
def checking_n(N):
    if N in range(1,100):

        if N %2 != 0:
            print ("Weird")
            return "Weird"
        elif N %2 == 0 and N in range(2,5):
            print("Not Weird")
            return "Not Weird"
        elif N%2==0 and N in range(6,20):
            print("Weird")
            return "Weird"
        elif N > 20:
            print("Not weird")
            return "Not weird"
    else:
        print("Try a number between a range of 1 to 100")


if __name__ == '__main__':
    N = int(input().strip())
    checking_n(N)