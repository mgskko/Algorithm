n = int(input())
k = list(map(int, input().split()))

k.sort()
print(sum(k)-max(k))