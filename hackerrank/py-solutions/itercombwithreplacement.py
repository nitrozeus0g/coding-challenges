#!/usr/bin/env python3

from itertools import combinations_with_replacement as cr


def main():
  s, k = input().strip().split()
  k = int(k)
  ret = [''.join(sorted(j)) for j in cr(s, k)]
  print('\n'.join(sorted(ret)))

if __name__ == '__main__':
  main()
