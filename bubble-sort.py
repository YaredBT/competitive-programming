#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(array):
    numswap = 0
    for i in range(len(array)-1):
        for j in range(len(array)-1):
        
            if(array[j] > array[j + 1]):
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
                numswap +=1
    print(f"Array is sorted in {numswap} swaps. \nFirst Element: {array[0]}\nLast Element: {array[len(array)-1]}")



if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
