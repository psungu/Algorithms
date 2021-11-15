#!/bin/python3

import math
import os
import random
import re
import sys


"""

Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. 
Then print the respective minimum and maximum values as a single line of two space-separated long integers.

"""

def miniMaxSum(arr):
    min_element = min(arr)
    max_element = max(arr)
    arr.remove(max_element)
    min_sum = sum(arr)
    arr.append(max_element)
    arr.remove(min_element)
    max_sum = sum(arr)
    print(min_sum, max_sum)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
