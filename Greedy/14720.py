n = int(input())
k = list(map(int, input().split()))
cnt = 0

for i in range(n):
    if (k[i] == cnt % 3):
        cnt += 1
print(cnt)
