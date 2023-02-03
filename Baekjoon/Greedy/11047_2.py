import sys
N, K = map(int, input().split())
coin = []
result = 0
for _ in range(N):
    coin.append(int(sys.stdin.readline()))

coin.sort(reverse=True)
for i in range(N):

    result += K // coin[i]
    K %= coin[i]
print(result)
