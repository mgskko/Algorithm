N = int(input())
M = list(map(int, input().split()))
num = 0
M.sort()

for i in range(N):
        for j in range(i + 1):
                 num += M[j]
print(num)