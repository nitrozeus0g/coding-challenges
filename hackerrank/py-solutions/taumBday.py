#!/usr/bin/env python3

import math
import os
import random
import re
import sys

#
# Complete the 'taumBday' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER b
#  2. INTEGER w
#  3. INTEGER bc
#  4. INTEGER wc
#  5. INTEGER z
#
# outputs: 20, 37, 12, 35, 12

def taumBday(b, w, bc, wc, z):
  # check if bc > wc+z or wc > bc+z
  if bc > (wc+z):
    x = (b+w)*wc+(b*z)
    print(x)
  elif wc > (bc+z):
    x = (w+b)*bc+(w*z)
    print(x)
  else:
    x = (b*bc)+(w*wc)
    print(x)

if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        b = int(first_multiple_input[0])
        w = int(first_multiple_input[1])
        second_multiple_input = input().rstrip().split()
        bc = int(second_multiple_input[0])
        wc = int(second_multiple_input[1])
        z = int(second_multiple_input[2])
        result = taumBday(b, w, bc, wc, z)
