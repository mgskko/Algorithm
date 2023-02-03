import sys
t = int(sys.stdin.readline())
k = []
for i in range(t):
  n = int(sys.stdin.readline())
  result = list(map(int, sys.stdin.readline().split()))
  k.append(result)
  print(min(k[i]),max(k[i]))