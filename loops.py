
import math
import os
import random
import re
import sys
def check_multiple(n):
    if n not in range(2,20):
        print("Please try a number between 2 and 20")
    else: 
        list = range(1,11)
        for i in list:
            print(f"{n} X {i} = {n * i}")                  

if __name__ == '__main__':
    n = int(input().strip())
    check_multiple(n)
