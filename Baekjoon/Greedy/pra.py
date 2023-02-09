n = int(input())
x = list(map(int,input().split()))
t = 0
result = []
x.sort(reverse=True)
for i in range(n):
  result.append(x[i] + i)
print(max(result) + 2)
