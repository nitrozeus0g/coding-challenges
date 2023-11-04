#!/usr/bin/env python3

def search(nums, t):
  if t not in nums:
    return -1
  start = 0
  end = len(nums) - 1
  while start <= end:
    mid = (start + end) // 2
    if nums[mid] > t:
      end = mid - 1
    elif nums[mid] < t:
      start = mid + 1
    else:
      return mid
  

def main():
  nums = list(map(int, input().strip().split()))
  t = int(input())
  result = search(nums, t)

if __name__ == '__main__':
  main()
