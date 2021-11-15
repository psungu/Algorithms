#!/bin/python3

import math
import os
import random
import re
import sys

"""
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
Print the decimal value of each fraction on a new line with  places after the decimal.

"""

def plusMinus(arr):
    
    negative_count = len(list(filter(lambda x: (x < 0), arr)))
    
    # we can also do len(list1) - neg_count
    positive_count = len(list(filter(lambda x: (x > 0), arr)))

    zero_count = len(arr) - negative_count - positive_count
    
    print(positive_count/len(arr))
    print(negative_count/len(arr))
    print(zero_count/len(arr))
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
