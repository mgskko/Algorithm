import sys
input = sys.stdin.readline
n = int(input())
t = [list(map(int, input().split())) for i in range(n)]
t.sort(key = lambda x : (x[1], x[0]))

last = 0 # 회의의 마지막 시간을 저장할 변수
conut = 0 # 회의 개수를 저장할 변수

for i, j in t:
    if i >= last: # 시작시간이 회의의 마지막 시간보다 크거나 같을경우
        conut += 1
        last = j
print(conut)