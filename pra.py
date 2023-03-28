def dp(n, nums):
    dp = [0] * n
    dp[0] = nums[0]
    max_sum = nums[0]

    for i in range(1, n):
        dp[i] = max(dp[i-1] + nums[i], nums[i])
        max_sum = max(max_sum, dp[i])
    return max_sum

n = int(input())
nums = list(map(int, input().split()))
print(dp(n, nums))