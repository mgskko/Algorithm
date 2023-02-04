import sys

n = int(sys.stdin.readline())
k = []
for i in range(n):
  k.append(list(map(str, sys.stdin.readline().split())))
k.sort(key=lambda x: (int(x[0])))

for result in k:
  print(result[0], result[1])
