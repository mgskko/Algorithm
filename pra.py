import sys

input = sys.stdin.readline

# n: 동전의 가지 수, k: 만들고자 하는 금액
n, k = map(int, input().split())

# 각 동전의 가치를 입력받고 내림차순으로 정렬한다.
coin_values = sorted([int(input()) for _ in range(n)], reverse=True)

# 가치가 높은 동전부터 순서대로 선택하며, 선택한 동전들의 개수를 센다.
count = 0
for coin in coin_values:
    # 현재 선택한 동전의 가치가 k보다 작거나 같은 경우,
    # 해당 동전으로 k원을 만들 수 있다.
    if coin <= k:
        count += k // coin  # 해당 동전으로 만들 수 있는 최대 개수를 더해준다.
        k %= coin  # k원 중 선택한 동전으로 만든 부분을 뺀 나머지 금액을 계산한다.

# 동전 개수의 합을 출력한다.
print(count)
