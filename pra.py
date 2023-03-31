n = int(input())
p = list([int(input()) for i in range(n)])
p.reverse()
cnt = 0
for i in range(1,n):
    if p[i] >= p[i-1]:
        dif = p[i-1] - 1
        cnt += p[i] - dif
        p[i] = dif
        dif = 0
    
print(cnt)