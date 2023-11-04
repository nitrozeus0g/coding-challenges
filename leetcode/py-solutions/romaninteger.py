#!/usr/bin/env python3


def main():
  s = input()
  rn = dict(
      I = 1,
      IV = 4,
      V = 5,
      IX = 9,
      X = 10,
      XL = 40,
      L = 50,
      XC = 90,
      C = 100,
      CD = 400,
      D = 500,
      CM = 900,
      M = 1000)

  ret = 0
  check = 0
  for i in range(len(s)):
    if check > 0:
      check = 0
      continue
    if i == len(s)-1:
      ret += rn[s[i]]
      break
    x = s[i]+s[i+1]
    if x in rn:
      print(rn[x])
      ret += rn[x]
      check = 1
    else:
      print(rn[s[i]])
      ret += rn[s[i]]
  print(ret)



if __name__ == '__main__':
  main()
