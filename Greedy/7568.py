import sys
n = int(sys.stdin.readline())
data = []
t = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    data.append((a, b))

for i in range(n):
    c = 0
    for j in range(n):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            c += 1
    t.append(c + 1)

for d in t:
    print(d, end=" ")
