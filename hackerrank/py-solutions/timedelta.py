#!/usr/bin/env python3

from datetime import datetime


def time_delta(date1, date2):
	d = datetime.strptime(date1, '%a %d %b %Y %H:%M:%S %z')
	d2 = datetime.strptime(date2, '%a %d %b %Y %H:%M:%S %z')
	r = int((d-d2).total_seconds())
	return abs(r) 



def main():
	n = int(input())
	for _ in range(n):
		date1 = input()
		date2 = input()
		ret = time_delta(date1, date2)
		print(ret)
	


if __name__ == '__main__':
	main()
