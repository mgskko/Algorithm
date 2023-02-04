import sys

a, b = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
list = A + B
answer = ' '.join(map(str, sorted(list)))
print(answer)