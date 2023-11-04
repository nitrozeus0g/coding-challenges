#!/usr/bin/env python3

import math
import os
import random
import re
import sys

#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#
# output: 5, 2

def acmTeam(topic):
  top = 0
  count = 0
  k = 0
  while k != n:
    for i in range(k+1,n):
      c = 0
      for j in range(m):
        if topic[k][j] == '0' and topic[i][j] == '0':
          continue
        else:
          c += 1
      if c > top:
        top = c
        count = 1
      elif c == top:
        count += 1
      else:
        continue
    k += 1
  print(top, count, sep='\n')

  #first get permutations of n (team of 2)
  #second add sum of '1s' 

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    topic = []
    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)
    result = acmTeam(topic)
