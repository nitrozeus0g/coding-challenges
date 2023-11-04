#!/bin/python3

from itertools import combinations as c


def main():
  s, k = input().strip().split()
  k = int(k)
  for i in range(1, k+1):
    ret = [''.join(sorted(j)) for j in c(s, i)]
    print('\n'.join(sorted(ret)))

if __name__ == '__main__':
  main()
