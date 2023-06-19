from audioop import reverse
import math
import os
import random
import re
import sys


def turn_to_binary(number):
    if number < 0:
        return number
    else:
        new_list = []

        new_list.append(turn_to_binary(number/2))
        x = new_list.reverse()
        return x

if __name__ == '__main__':
    turn_to_binary(7)
