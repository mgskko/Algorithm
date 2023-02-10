n = int(input())
k = list(map(int, input().split()))
k1 = []

k.sort(reverse=False)
c = 0
for num in k:
  c += num
  k1.append(c)
print(sum(k1))
