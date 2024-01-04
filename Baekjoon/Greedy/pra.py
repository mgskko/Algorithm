import sys

n = int(sys.stdin.readline())
M = input()

count = int(M.count('LL'))

if count <= 1:
    print(len(M))
else :
    print(len(M) - count + 1)

