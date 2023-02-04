n=int(input())
setA = set(map(int,input().split()))
m=int(input())
setB = list(map(int,input().split()))

for x in setB:
    if x in setA:
        print(1)
    else:
        print(0)