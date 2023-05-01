t = int(input())  # 테스트 케이스 수

# 테스트 케이스 수 만큼 반복
for _ in range(t):
    k = int(input())  # 층 수
    n = int(input())  # 호 수

    # 아파트 초기화
    apt = [i for i in range(1, n+1)]

    # k층까지 각 호실의 사람 수 계산
    for i in range(k):
        for j in range(1, n):
            # 현재 호실의 사람 수에 이전 호실의 사람 수를 더함
            apt[j] += apt[j-1]

    # 마지막 호실의 사람 수 출력
    print(apt[-1])
