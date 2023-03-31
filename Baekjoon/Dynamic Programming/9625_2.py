n = int(input())  # 입력값 n을 받아옴
a = [0]*(n+1)  # a 리스트를 생성하고 0으로 초기화
a[1] = 1  # a[1]의 값을 1로 설정

for i in range(2,n+1):  # i가 2부터 n까지 반복
    a[i] = a[i-1] + a[i-2]  # a[i]를 a[i-1] + a[i-2]의 합으로 갱신

print(a[n-1],a[n])  # a[n-1]과 a[n] 출력