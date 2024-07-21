#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plus_minus(arr):
    # Write your code here
    n = len(arr)
    positves = 0
    negatives = 0
    zeros = 0
    
    for item in arr:
        if item == 0:
            zeros += 1
        if item > 0:
            positves += 1
        if item < 0:
            negatives += 1
    
    print(positves/n)
    print(negatives/n)
    print(zeros/n)
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plus_minus(arr)
