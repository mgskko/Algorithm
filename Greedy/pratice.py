import sys
n = int(sys.stdin.readline())
k = []
result = []

def s(k):
  k.sort(reverse=True)
  for j in range(n):
    k[j] = k[j] * (j + 1)
  return max(k)



for i in range(n):
  k.append(int(sys.stdin.readline()))

print(s(k))