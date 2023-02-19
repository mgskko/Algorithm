n = int(input())
n1 = set(map(int,input().split()))
m = int(input())
m1 = list(map(int,input().split()))
k = []
for i in m1:
    if i in n1:
        k.append(1)
    else:
        k.append(0)
print(*k)