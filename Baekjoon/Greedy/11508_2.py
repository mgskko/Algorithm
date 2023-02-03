import sys

n = int(sys.stdin.readline())
k = []
result = 0
for _ in range(n):
    k.append(int(sys.stdin.readline()))
k.sort(reverse=True)

result = 0
for i in range(2, len(k), 3):
    result += k[i]

print(sum(k)-result)
