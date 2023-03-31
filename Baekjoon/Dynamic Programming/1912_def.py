def dp(n, nums):
    # n 크기의 리스트 생성
    dp = [0] * n
    # 첫번째 수로 초기화
    dp[0] = nums[0]
    # 최대 합
    max_sum = nums[0]

    # 두번째 수부터 끝까지
    for i in range(1, n):
        # 현재 수를 포함하는 연속된 수열의 최대 합
        dp[i] = max(dp[i-1] + nums[i], nums[i])
        # 최대 합 갱신
        max_sum = max(max_sum, dp[i])
    # 최대 합 반환
    return max_sum

# 수열의 길이 입력받기
n = int(input())
# 수열 입력받기
nums = list(map(int, input().split()))
# 최대 연속합 구하기
print(dp(n, nums))
