#!/usr/bin/env python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k,s):
  x = [0] * k
  for n in s:
    x[n%k] += 1
  ret = min(x[0],1) 
  for i in range(1,k//2+1):
    if i != k-i:
      ret += max(x[i], x[k-i])
  if k%2 == 0:
    ret += 1
  print(ret)

if __name__ == '__main__':
  first_multiple_input = input().rstrip().split()
  n = int(first_multiple_input[0])
  k = int(first_multiple_input[1])
  s = list(map(int, input().rstrip().split()))
  result = nonDivisibleSubset(k, s)
