n = int(input())  # 수열의 길이 입력받기
nums = list(map(int, input().split()))  # 수열 입력받기

dp = [0] * n  # DP 테이블 초기화
dp[0] = nums[0]  # 초기값 설정
max_sum = nums[0]  # 최대 연속합을 저장할 변수 초기화

for i in range(1, n):
    dp[i] = max(dp[i-1] + nums[i], nums[i])  # DP 점화식
    max_sum = max(max_sum, dp[i])  # 최대 연속합 갱신

print(max_sum)  # 최대 연속합 출력
