#!/usr/bin/env/ python3

#PDFviewer
import string

def main():
  n = input().split(" ")
  word = input()
  thebet = list(string.ascii_lowercase)
  d = {x: int(y) for x, y in zip(thebet, n)}
  ret = 0

  for i in word:
    temp = d.get(i)
    #print(temp)
    if int(temp) > ret:
      ret = temp

  print(ret * len(word))

if __name__ == '__main__':
  main()
