# 정수 n을 입력받습니다.
n = int(input())

# DP 테이블 dp를 생성합니다.
# 여기서 dp[i]는 i번째 사다리를 올라가는 최소 이동 횟수를 의미합니다.
dp = [-1] * (n+8)

# 초기값을 설정합니다.
dp[2]=1
dp[4]=2
dp[5]=1
dp[6]=3
dp[7]=2
dp[8]=4

# DP를 실행합니다.
for i in range(9,n+1):
    dp[i] = min(dp[i-2],dp[i-5]) + 1

# n번째 사다리를 올라가는 최소 이동 횟수를 출력합니다.
print(dp[n])
