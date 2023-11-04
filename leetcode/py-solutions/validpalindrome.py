#!/usr/bin/env python3

s = 'A man, a plan, a canal: Panama'

def main():
  x = ''.join(i for i in s if i.isalpha() or i.isnumeric()).lower()
  print(x)

if __name__ == '__main__':
  main()


