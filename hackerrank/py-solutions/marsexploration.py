#!/usr/bin/env python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
  
  x = len(s)//3
  ret = 0

  for i in range(0, len(s), 3):
    if s[i] != 'S':
      ret += 1
    if s[i+1] != 'O':
      ret += 1
    if s[i+2] != 'S':
      ret += 1
  print(ret)


if __name__ == '__main__':
  s = input()
  result = marsExploration(s)
