import sys
input = sys.stdin.readline

n = int(input())
k = [list((map(int,input().split()))) for _ in range(n)]
dp = [0]*(n+1)

for i in range(n-1,-1,-1):
    if k[i][0] + i > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], k[i][1] + dp[i + k[i][0]])
print(max(dp))