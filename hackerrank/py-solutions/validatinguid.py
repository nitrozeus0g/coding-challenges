#!/usr/bin/env python3

import re

def main():
	n = int(input())

	for _ in range(n):
		x = input()
		upp = sum(1 for i in re.finditer('[A-Z]', x))
		num = sum(1 for i in re.finditer('[0-9]', x))

		if len(x) != 10:
			print('Invalid')
		elif re.match('[^a-zA-Z0-9]', x):
			print('Invalid')
		elif upp < 2 or num < 3:
			print('Invalid')
		elif len(set(x)) != 10:
			print('Invalid')
		else:
			print('Valid')
	

if __name__ == '__main__':
	main()
