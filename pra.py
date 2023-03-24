n = int(input())
s = [0 for i in range(301)]
dp = [0 for i in range(301)]

for i in range(1, n+1):
    s[i] = int(input())

dp[1] = s[1]
dp[2] = s[1] + s[2]
dp[3] = max(s[2]+s[3],s[1]+s[3])

for i in range(4,n+1):
    dp[i] = max(s[i] + s[i-1] + dp[i-3], s[i] + dp[i-2])

print(dp[n])