#!/usr/bin/env python3

l1 = [1, 2, 3, 0, 0, 0]
l2 = [2, 5, 6]

def main():
  idx = 0
  for i in range(len(l1)):
    if l1[i] == 0:
      l1[i] = l2[idx]
      idx += 1
  print(sorted(l1))

if __name__ == '__main__':
  main()


