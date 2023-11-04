#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jimOrders' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY orders as parameter.
#

def jimOrders(orders):
	x = {j+1: sum(i) for j, i in enumerate(orders)}
	y = dict(sorted(x.items(), key=lambda item: item[1]))
	print(' '.join(str(i) for i, j in y.items()))
	
if __name__ == '__main__':

    n = int(input().strip())

    orders = []

    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))

    result = jimOrders(orders)

