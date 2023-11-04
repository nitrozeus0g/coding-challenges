#!/usr/bin/env python3

from collections import OrderedDict

def main():
	n = int(input())
	od = OrderedDict()

	for i in range(n):
		x = input().split()
		key = ' '.join(i for i in x[:-1])
		value = int(x[-1])
		od.setdefault(key, []).append(value)
		
	for k, v in od.items():
		print(f'{k} {sum(v)}')
		

if __name__ == '__main__':
	main()
