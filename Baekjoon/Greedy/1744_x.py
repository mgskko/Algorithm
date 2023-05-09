import sys
input = sys.stdin.readline

n = int(input())
t = [int(input()) for _ in range(n)]
t.sort()
arr = []
plus = 0
mu = 0
if n == 1:
    print(sum(t))
elif (n%2) == 0:
    for i in range(0, n, 2):
        plus += t[i] + t[i + 1]
        mu += t[i] * t[i + 1]
        if plus >= mu:
            arr.append(plus)
        else:
            arr.append(mu)
        plus = 0
        mu = 0
    print(sum(arr))
elif (n%2) == 1:
    for i in range(0, n-1, 2):
        plus += t[i] + t[i + 1]
        mu += t[i] * t[i + 1]
        if plus >= mu:
            arr.append(plus)
        else:
            arr.append(mu)
        plus = 0
        mu = 0
    print(sum(arr)+t[-1])
## 반례) 홀수일경우  -537,-435,81,157,257