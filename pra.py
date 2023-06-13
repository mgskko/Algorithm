import sys
input = sys.stdin.readline

# 입력을 받아옵니다.
n = int(input())

s = list(map(int,input().split()))
s.sort()
t = 0
#홀수이면
if (n % 2) == 1:
    for i in range(((n-1)//2)):
        t = max((s[i] + s[n-i-2]), t)
    print(t)

else:
    for i in range(n//2):
        t = max((s[i] + s[n-i-1]), t)
    print(t)
