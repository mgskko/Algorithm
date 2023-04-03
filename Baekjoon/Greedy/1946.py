import sys
input = sys.stdin.readline
c = int(input())
for i in range(c):
    n = int(input())
    k = []
    for _ in range(n):
        a, b = (map(int,input().split()))
        k.append((a,b))

    k.sort(key=lambda x:x[0])
    cnt = 1
    min = k[0][1]
    for i in range(1,n):
        if k[i][1] < min:
            min = k[i][1]
            cnt += 1
    print(cnt)
