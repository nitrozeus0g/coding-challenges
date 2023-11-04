#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#
# input1 s/e 4
# input2 s/e 3

def jumpingOnClouds(c):
  ret = 0
  idx = 0
  while idx < len(c)-1:
    if idx+1 == len(c)-1:
      ret += 1
      break
    if c[idx+2] == 0:
      ret += 1
      idx += 2
    else:
      ret += 1
      idx += 1
  print(ret)

if __name__ == '__main__':
  n = int(input().strip())
  c = list(map(int, input().rstrip().split()))
  result = jumpingOnClouds(c)

