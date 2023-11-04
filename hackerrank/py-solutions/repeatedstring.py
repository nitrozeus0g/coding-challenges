#!/usr/bin/env/ python3

def main():
	s = input()
	n = int(input())
	x, y =divmod(n, len(s))
	print(s[:y].count('a')*(x+1)+s[y:].count('a')*x)


if __name__ == '__main__':
  main()
