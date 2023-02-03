N, K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))
coins.sort(reverse=True)

a=0
for coin in coins:
    if K >= coin:
        a += K // coin
        K %= coin
        if K <= 0:
            break
print(a)