n = int(input())  # 테스트 케이스 수 입력

dp = [1] * 101  # 초기화: dp 리스트에 1을 101개 담는다.
dp[4] = 2  # 초기화: dp[4]와 dp[5]는 2로 세팅한다.
dp[5] = 2

for _ in range(n):  # n번 반복한다.
    k = int(input())  # k 입력받기

    # dp 리스트의 인덱스 6부터 k까지 반복하여 dp 값을 구한다.
    for i in range(6, k+1):
        dp[i] = dp[i-5] + dp[i-1]

    print(dp[k])  # dp[k] 값을 출력한다.

# 시간 복잡도 O(n^2)
