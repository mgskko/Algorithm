# 입력값 n을 받는다.
n = int(input())

# dp 리스트를 0으로 초기화한다.
dp = [0] * 101

# dp 리스트의 초기값을 설정한다.
dp[1], dp[2], dp[3] = 1, 1, 1

# dp 리스트를 채운다.
for i in range(4, 101):
    dp[i] = dp[i-2] + dp[i-3]

# 입력값 k를 받고, k번째 항의 값을 출력한다.
for _ in range(n):
    k = int(input())
    print(dp[k])



# 시간 복잡도 O(n)