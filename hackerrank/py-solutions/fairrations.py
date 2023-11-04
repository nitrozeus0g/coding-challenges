#!/usr/bin/env python3

def fairRations(n, b):
	ret = 0
	for i in range(n-1):
		if b[i] % 2 != 0:
			b[i] += 1
			b[i+1] += 1
			ret += 2
	if b[n-1] % 2 == 0:
		print(ret)
	else:
		print('NO')

def main():
	n = int(input().strip())
	b = list(map(int, input().strip().split()))
	result = fairRations(n, b)

if __name__ == '__main__':
	main()
