#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

def kaprekarNumbers(p, q):
	kaprekar_nums = []
	for num in range(p, q + 1):
		square = num * num
		str_square = str(square)
		if len(str_square) == 1:
			if square == i:
				kaprekar_nums.append(num)
		else:

			split_idx = len(str_square) // 2
			left_part = int(str_square[:split_idx])
			right_part = int(str_square[split_idx:])

			if left_part + right_part == num:
				kaprekar_nums.append(num)
	if not kaprekar_nums:
		print("INVALID RANGE")
	else:
		print(' '.join(map(str, kaprekar_nums)))

		

if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
