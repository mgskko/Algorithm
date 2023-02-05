n = int(input())
k = []
k1 = []
result = 0
for i in range(n):
    k.append(int(input()))
k.sort(reverse=True)

for i in range(n):
    if (k[i]-i) > 0: 
        k1.append(k[i]-i)
print(k1)

