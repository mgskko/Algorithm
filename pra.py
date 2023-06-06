import sys
input = sys.stdin.readline

# 입력을 받아옵니다.
n = int(input())

# 입력된 값들을 저장할 리스트를 생성합니다.
s = []

# 결과를 저장할 변수를 초기화합니다.
t = 0

# n번 반복하면서 입력값을 리스트에 추가합니다.
for i in range(n):
    s.append(int(input()))

# 입력값들을 오름차순으로 정렬합니다.
s.sort()

# 1부터 n까지 반복하면서 각 값과 해당 인덱스의 차이의 절댓값을 결과 변수에 누적합니다.
for i in range(1, n+1):
    t += abs(i - s[i-1])

# 결과를 출력합니다.
print(t)
