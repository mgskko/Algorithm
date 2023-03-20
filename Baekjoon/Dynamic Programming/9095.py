n = int(input())

for i in range(n):
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
        for j in range(4,11):
            dp[j] = dp[j-1]+dp[j-2]+dp[j-3]
        print(dp[k])