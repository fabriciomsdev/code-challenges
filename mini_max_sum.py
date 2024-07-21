#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def mini_max_sum(arr):
    # Write your code here
    arr.sort()
    lowest = sum(arr[:-1])
    greatest = sum(arr[1:])
    
    print(lowest, greatest)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    mini_max_sum(arr)
