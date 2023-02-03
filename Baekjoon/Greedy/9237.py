import sys
n = int(sys.stdin.readline())
t = list(map(int, input().split()))
result = 0
t.sort(reverse=True)

for i in range(n):
    t[i] = t[i] + i + 2
print(max(t))
