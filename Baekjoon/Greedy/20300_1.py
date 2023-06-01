import sys

# 입력값을 더 효율적으로 받기 위해 sys.stdin.readline을 사용합니다.
input = sys.stdin.readline

# 정수 n을 입력받습니다.
n = int(input())

# 정수들을 리스트 t에 입력받고 오름차순으로 정렬합니다.
t = list(map(int, input().split()))
t.sort()

# 합을 저장할 리스트 k와 합이 홀수인 경우를 처리하기 위한 조건문을 설정합니다.
cnt = 0
k = []
if (len(t) % 2) == 1:
    k.append(t.pop(-1))

# t 리스트의 원소들을 순회하며 가장 큰 합을 계산합니다.
for i in range(len(t)):
    # t[i]가 t의 대칭되는 원소보다 큰 경우에는 더 이상 계산하지 않고 종료합니다.
    if t[i] > t[(len(t)-i-1)]:
        break
    # t[i]와 대칭되는 원소의 합을 k 리스트에 추가합니다.
    k.append(t[i]+t[(len(t)-i-1)])

# k 리스트의 최댓값을 출력합니다.
print(max(k))
