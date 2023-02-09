import sys
N = int(sys.stdin.readline())
num = []
result = 0
k = 2

for _ in range(N):
    num.append(int(sys.stdin.readline()))
num.sort(reverse = True)

for i in range(N):
    if (i == k):
        k+=3
        continue
    result += num[i]
print(result)