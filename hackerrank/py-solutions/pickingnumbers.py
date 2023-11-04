#!/usr/bin/env python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
  x = {i: a.count(i) for i in a}
  ret = 0
  for i in a:
    t = x[i] + x.get(i+1, 0)
    if ret < t:
      ret = t
  print(ret)

if __name__ == '__main__':
  n = int(input().strip())
  a = list(map(int, input().rstrip().split()))
  result = pickingNumbers(a)
