t = int(input())
k = []
for _ in range(t):
  k.append(list(map(int,input().split())))

for i in range(t):
  k[i].remove(max(k[i]))
  k[i].remove(min(k[i]))
  if max(k[i])-min(k[i]) >= 4:
    print("KIN")
  else:
    print(sum(k[i]))