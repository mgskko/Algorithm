import sys

n = int(sys.stdin.readline())
A = []

for i in range(n):
    A.append(sys.stdin.readline().strip())
A = list(set(A))
A.sort()
A.sort(key = len) 
for i in A:
    print(i)
