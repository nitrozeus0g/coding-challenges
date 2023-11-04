#!/usr/bin/env python3

import re

def main():
  m = re.search(r'([A-Za-z0-9])\1+', input())
  if m:
    print(m.group(1))
  else:
    print(-1)

if __name__ == '__main__':
  main()
