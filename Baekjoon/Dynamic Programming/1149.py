n = int(input())
k=[]
for i in range(n):
    k.append(list(map(int,input().split())))
for i in range(1, n):
    k[i][0] += min(k[i-1][1],k[i-1][2])
    k[i][1] += min(k[i-1][0],k[i-1][2])
    k[i][2] += min(k[i-1][0],k[i-1][1])

result = min(k[n-1][0], k[n-1][1], k[n-1][2])
print(result)