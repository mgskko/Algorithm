import sys
input = sys.stdin.readline

# 입력을 받아옵니다.
n = int(input())  # 정수의 개수
k = int(input())  # 선택할 정수의 개수
s = list(map(int, input().split()))  # 정수들의 리스트
s.sort()  # 정수들을 오름차순으로 정렬합니다.

array = []
for i in range(0, n-1):
    # 인접한 정수들 간의 차이를 구하여 array 리스트에 추가합니다.
    array.append(s[i+1] - s[i])
array.sort()  # 정수들의 차이를 오름차순으로 정렬합니다.

# 가장 작은 (n-k)개의 정수들의 합을 계산하여 출력합니다.
print(sum(array[:n-k]))
