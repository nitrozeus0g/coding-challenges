#!/usr/bin/env python3

def main():
  s = list(map(int, input().strip().split()))
  x = {i: s.count(i) for i in s}
  k = list(x.keys())
  v = list(x.values())
  pos = v.index(1)
  print(k[pos])

if __name__ == '__main__':
  main()
