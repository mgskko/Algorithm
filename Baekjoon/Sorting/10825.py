n = int(input())
k = list([input().split() for _ in range(n)])
k.sort(key=lambda x : (-int(x[1]), int(x[2]),-int(x[3]), x[0]))

for i in k:
    print(i[0])