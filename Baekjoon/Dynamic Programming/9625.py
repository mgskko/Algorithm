# n을 입력 받음
n = int(input())

# a 리스트를 n+1 크기로 생성하고, 0으로 초기화
a = [0]*(n+1)

# a[1]을 1로 초기화
a[1] = 1

# a[i]를 i-1번째와 i-2번째의 합으로 계산
for i in range(2,n+1):
    a[i] = a[i-1] + a[i-2]

# a[n-1]과 a[n]을 출력
print(a[n-1],a[n])