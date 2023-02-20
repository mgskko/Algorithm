import sys

n = int(sys.stdin.readline())
k = list(map(int, sys.stdin.readline().split()))
m = []

for i in k:
    a = 0
    for j in k:
        a += abs(i - j)
    m.append(a)
print(min(m))