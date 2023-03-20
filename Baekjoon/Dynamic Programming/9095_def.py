def dp(k):
    if k == 1:
        return 1
    elif k == 2:
        return 2
    elif k == 3:
        return 4
    else:
        return dp(k-3) + dp(k-2) + dp(k-1)

n = int(input())

for i in range(n):
    print(dp(int(input())))