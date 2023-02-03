import sys
n = int(sys.stdin.readline())
k = []
result = []
for i in range(n):
  k.append(int(sys.stdin.readline()))
k.sort(reverse=True)
for num in range(n):
  result.append(k[num] * (num+1))
print(max(result))