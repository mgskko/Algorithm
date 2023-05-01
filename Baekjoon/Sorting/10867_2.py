n = int(input())
t = list(map(int, input().split()))

for i in sorted(list(set(t))): #set으로 중복 방지, sorted로 정렬
    print(i, end = ' ')