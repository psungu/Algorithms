import math
import os
import random
import re
import sys

"""
Staircase detail

This is a staircase of size :

   #
  ##
 ###
####

Its base and height are both equal to . It is drawn using # symbols and spaces. The last line is not preceded by any spaces.

Write a program that prints a staircase of size .


"""


def staircase(n):
    for i in range(n):
        print(' '*(n-i-1)+'#'*(i+1))

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)