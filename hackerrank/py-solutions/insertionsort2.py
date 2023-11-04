#!/usr/bin/env python3
import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
  for i in range(1, n):
    x = arr[i]
    y = i - 1
    while y >= 0 and x < arr[y]:
      arr[y + 1] = arr[y]
      y -= 1
    arr[y + 1] = x
    ret = [str(i) for i in arr]
    print(' '.join(ret))



  

    
if __name__ == '__main__':
  n = int(input().strip())
  arr = list(map(int, input().rstrip().split()))
  insertionSort2(n, arr)



