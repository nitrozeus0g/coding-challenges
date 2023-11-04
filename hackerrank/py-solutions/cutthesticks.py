#!/usr/bin/env python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
# 1 <= n <= 1000
# 1 <= arr[i] <= 1000

def cutTheSticks(arr):
  y = len(arr)
  arr.sort()
  x = 0
  for i in arr:
    if i != x:
        print(y)
    x = i
    y -= 1

if __name__ == '__main__':
  n = int(input().strip())
  arr = list(map(int, input().rstrip().split()))
  result = cutTheSticks(arr)


# output #
#8
#6
#4
#1
