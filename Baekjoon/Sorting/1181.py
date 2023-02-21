import sys

n = int(sys.stdin.readline())
A = list(sys.stdin.readline().strip() for _ in range(n))

A = list(set(A))
A.sort()
A.sort(key = len) 
for i in A:
    print(i)
