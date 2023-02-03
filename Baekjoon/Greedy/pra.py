n = int(input())
k = []
k2 = 0
for _ in range(n):
  k.append(int(input()))

k.sort(reverse=True)

for i in range(n):
  result = k[i]-i
  if result > 0:
    k2 += (result)
print(k2)