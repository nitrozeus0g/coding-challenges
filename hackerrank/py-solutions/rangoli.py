#!/usr/bin/env python3




def print_rangoli(size):
  a = 'abcdefghijklmnopqrstuvwxyz'
  d = '-'
  x = [a[i] for i in range(n)]
  l = list(range(n))
  l2 = l[:-1]+l[::-1]
  for i in l2:
    y = x[-(i+1):]
    z = y[::-1]+y[1:]
    print(d.join(z).center(n*4-3,d))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
