n = int(input())
result = []
for _ in range(n):
  result.append(list(map(int, input().split())))

result.sort(key=lambda x: (x[0], x[1]))

for i in result:
  print(i[0],i[1])