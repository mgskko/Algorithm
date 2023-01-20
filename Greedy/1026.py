import sys
N = int(sys.stdin.readline())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
S = 0
for _ in range(N):
    A_max = max(A)
    B_min = min(B)
    S += A_max * B_min
    A.pop(A.index(A_max))
    B.pop(B.index(B_min))
print(S)
