import sys
n = list(map(int, input().split()))
k = list(map(int, input().split()))

k.sort(reverse=False)

for i in k:
    if n[1] >= i:
        n[1] += 1
    else:
        break
print(n[1])
