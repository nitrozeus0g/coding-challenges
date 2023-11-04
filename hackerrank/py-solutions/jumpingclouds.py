#!/usr/bin/env python3

import math
import os
import random
import re
import sys

### Jumping on the Clouds: Revisited
# 2py = 92, 3py = 80(i think)

# Need to figure out how to loop around until i lands back on c[0]
# while loop
def jumpingOnClouds(c, k):
  e = 100
  x = 0
  while x < n:
    x += k
    if c[x] == 0:
      e -= 1
    if c[x] == 1:
      e -= 3
    if (x+k) % n == 0:
      if c[0] == 0:
        e -= 1
      else:
        e -= 3
      print(e)
      break
    if x+k > (n+1)-k:
        x = (x+k) % (n)-k

if __name__ == '__main__':
  nk = input().split()
  n = int(nk[0])
  k = int(nk[1])
  c = list(map(int, input().rstrip().split()))
  result = jumpingOnClouds(c, k)


