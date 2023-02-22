a, b = map(int,input().split())
n = list(map(int,input().split()))
m = list(map(int,input().split()))
c = n + m
c.sort(reverse=True)
print(*c)