n = int(input())
k = []
for _ in range(n):
  k.append(int(input()))

c = 0
for i in range(n-1,0,-1):
  if k[i] <= k[i - 1]:
    c += (k[i - 1] - k[i] + 1)
    k[i - 1] = k[i] - 1
print(c)
