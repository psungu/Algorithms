import math
import os
import random
import re
import sys


"""

Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

"""


def timeConversion(s):
    result = s[:-2]
    if(s[-2:] == 'AM' and s[:2]=='12'):
        result = str('00'+ s[2:8])
    elif(s[-2:]=='PM' and s[:2]!='12'):
        result = str(int(s[:2]) + 12) + s[2:8]
        
    return result
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
