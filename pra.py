n = int(input())
for _ in range(n):
    k = int(input())
    if k == 1:
        print(1)
    elif k == 2:
        print(2)
    elif k == 3:
        print(4)
    else:
        dp = [0] * 11
        dp[1] = 1
        dp[2] = 2
        dp[3] = 4
        for i in range(4,11):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[k])
