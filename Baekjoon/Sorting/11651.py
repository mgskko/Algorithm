import sys

n = int(sys.stdin.readline())
k = []
for i in range(n):
  k.append(list(map(int, sys.stdin.readline().split())))

k.sort(key=lambda x: (x[1], x[0]))

for result in k:
  print(result[0], result[1])
