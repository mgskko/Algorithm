import sys
input = sys.stdin.readline

# 입력 받기
n = int(input())
k = [list(map(int,input().split())) for _ in range(n)]

# dp 테이블 초기화
dp = [0] *(n+1)

# 뒤에서부터 dp 진행
for i in range(n-1,-1,-1):
    if i + k[i][0] > n: # 인덱스 범위를 초과하는 경우, 현재 위치의 값은 다음 값으로 업데이트
        dp[i] = dp[i+1]
    else: # 인덱스 범위 내에 있는 경우, 뒤에 있는 값들과 현재 위치의 값을 비교해서 최대값을 저장
        dp[i] = max(dp[i+1], k[i][1] + dp[i + k[i][0]])

# dp 테이블에서 최대값 출력
print(max(dp))
