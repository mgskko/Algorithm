n = int(input())
dp = [0]*1000
dp[1] = 1
dp[2] = 2

for i in range(3,1000):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[n]%10007)
