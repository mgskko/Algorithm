import sys
n = int(sys.stdin.readline())
k = []

for i in range(n):
  k.append(int(sys.stdin.readline()))
k.sort(reverse=False)

for i in range(n):
  print(k[i])