from itertools import product as p

k, m = list(map(int, input().split()))
arr = []
for i in range(k):
  arr.append(list(map(int, input().split()[1:])))
  
ret = []
x = p(*arr)
for i in x:
  ret.append(sum(j*j for j in i)%m)
  
print(max(ret))
    
