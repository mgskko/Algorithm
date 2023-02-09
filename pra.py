import sys
n, m = list(map(int,sys.stdin.readline().split()))
n1 = list(map(int,sys.stdin.readline().split()))

n1.sort(reverse=False)

print(n1[m-1])