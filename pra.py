n, l = map(int, input().split())
k = list(map(int,input().split()))
k.sort(reverse=False)
start = k[0]
end = k[0] + l
cnt = 1
for i in range(n):
    if start <= k[i] < end:
        continue
    else:
        start = k[i]
        end = k[i] + l
        cnt += 1
print(cnt)