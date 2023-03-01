import sys

n = int(sys.stdin.readline())

for i in range(n):
    n,m = map(int,input().split())
    print("Case #{0}: {1}".format(i+1,n+m))