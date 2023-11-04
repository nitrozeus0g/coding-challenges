#!/usr/bin/env python3

from collections import Counter

def main():
	n = int(input())
	x = [input() for i in range(n)]
	z = Counter(x)
	#y = {i: x.count(i) for i in x}
	print(len(set(x)))
	#print(*y.values(), sep=' ')
	print(*z.values(), sep=' ')
	




if __name__ == '__main__':
	main()
