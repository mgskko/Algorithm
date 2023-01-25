import sys
n = int(sys.stdin.readline())
data = []
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    data.append((x, y))
print(data)
