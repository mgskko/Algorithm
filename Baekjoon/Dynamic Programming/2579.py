n = int(input())
s = [0 for i in range(301)]
dp = [0 for i in range(301)]
for i in range(n):
    s[i] = int(input())
dp[0] = s[0]
dp[1] = s[0] + s[1]
dp[2] = max((s[0] + s[2]),(s[1] + s[2]))
for i in range(3,n):
    dp[i] = max((s[i]+s[i-1]+dp[i-3]),(s[i]+dp[i-2]))
print(dp[n-1])