import sys

# 입력값을 더 효율적으로 받기 위해 sys.stdin.readline을 사용합니다.
input = sys.stdin.readline

# 정수 n을 입력받습니다.
n = int(input())

# 정수들을 리스트 t에 입력받고 오름차순으로 정렬합니다.
t = list(map(int, input().split()))
t.sort()

k = 0

if (n % 2) == 1:  # n이 홀수인 경우
    # 중간 값과 대칭되는 원소들 중 큰 값을 선택하여 k에 저장합니다.
    for i in range((n-1) // 2):
        k = max((t[i] + t[n-i-2]), k)
    print(k)
else:  # n이 짝수인 경우
    # 중간 값을 기준으로 좌우 대칭되는 원소들 중 큰 값을 선택하여 k에 저장합니다.
    for i in range(n // 2):
        k = max((t[i] + t[n-i-1]), k)
    print(k)
