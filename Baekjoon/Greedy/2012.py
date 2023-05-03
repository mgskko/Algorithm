import sys
n = int(sys.stdin.readline())
t = [int(sys.stdin.readline()) for _ in range(n)]
# n개의 정수를 입력 받아 리스트 t에 저장한다.

cnt = 0

t.sort()
# 리스트 t를 오름차순으로 정렬한다.

for i in range(1, n+1):
    cnt += abs(i - t[i-1])
    # 1부터 n까지의 수와 정렬된 리스트 t의 원소의 차이를 누적해서 계산한다.

print(cnt)
# 결과값을 출력한다.
