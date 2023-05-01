# 정수 n을 입력받습니다.
n = int(input())

# 필요한 5와 2의 최소 개수를 구하는 변수 result를 초기화합니다.
result = 0

# 무한 루프를 돌면서 5로 나누어 떨어지는지 확인합니다.
while True:
    # 만약 5로 나누어 떨어진다면, result에 (n // 5)를 더한 후 결과를 출력하고 루프를 빠져나갑니다.
    if n % 5 == 0:
        result += (n // 5)
        print(result)
        break
    # 5로 나누어 떨어지지 않는다면, n에서 2를 빼고 result에 1을 더합니다.
    else :
        n -= 2
        result += 1
    # 만약 n이 0보다 작아진다면, 5와 2로 나타낼 수 없으므로 -1을 출력하고 루프를 빠져나갑니다.
    if n < 0:
        print(-1)
        break
