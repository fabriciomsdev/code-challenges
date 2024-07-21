#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def time_conversion(s):
    # Write your code here
    hour, minutes, seconds = s.split(':')
    seconds, time = seconds[0:2], seconds[2:4]
    hour = int(hour)

    if time == 'AM' and hour == 12:
        hour = 0
    if time == 'PM':
        if hour < 12:
            hour += 12
    if hour < 10:
        hour = f'0{hour}'

    return f'{hour}:{minutes}:{seconds}'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = time_conversion(s)

    fptr.write(result + '\n')

    fptr.close()
