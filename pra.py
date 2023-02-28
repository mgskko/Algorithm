n = int(input())

m = []
for i in range(n):
    m.append(input().split())

m.sort(key=lambda x:int(x[0]))
m.sort(key=lambda x:x[1])

for result in m:
  print(result[0], result[1])

