import sys

def dp(k):
    if k == 1:
        return 1
    elif k == 0:
        return 0
    else:
        return dp(k-1)+dp(k-2)

n = int(sys.stdin.readline())
print(dp(n))


