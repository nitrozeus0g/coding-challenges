#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
  x = arr[::-1]
  y = arr[::-1]
  for i in range(n-1):
    if y[i] < x[i+1]:
      x[i] = y[i+1]
      y[i+1] = y[i]
      ret = [str(i) for i in x[::-1]]
      print(' '.join(ret))
      x[i+1] = y[i]
    else:
      x[i] = y[i]
  ret = [str(i) for i in x[::-1]]
  print(' '.join(ret))
      


if __name__ == '__main__':
  n = int(input().strip())

  arr = list(map(int, input().rstrip().split()))

  insertionSort1(n, arr)

