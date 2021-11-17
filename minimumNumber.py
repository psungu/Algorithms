#!/bin/python3

import math
import os
import random
import re
import sys

"""
Louise joined a social networking site to stay in touch with her friends. 
The signup page required her to input a name and a password. However, the password must be strong. 
The website considers a password to be strong if it satisfies the following criteria:

Its length is at least .
It contains at least one digit.
It contains at least one lowercase English character.
It contains at least one uppercase English character.
It contains at least one special character. The special characters are: !@#$%^&*()-+
She typed a random string of length  in the password field but wasn't sure if it was strong. Given the string she typed, 
can you find the minimum number of characters she must add to make her password strong?

"""

def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    
    result1 = max(0, 6-n)
    result2 = 0
    
    if(result1>=0):
        if not any(c in password for c in lower_case):
            result2 += 1
        if not any(c in password for c in upper_case):
            result2 += 1
        if not any(c in password for c in numbers):
            result2 += 1
        if not any(c in password for c in special_characters):
            result2 += 1
        
    return max(result1, result2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
