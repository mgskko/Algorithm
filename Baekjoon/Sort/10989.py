import sys

N = int(input())

P = [0] * 10001

for i in range(N):
    input_num = int(sys.stdin.readline())
    
    P[input_num] = P[input_num] + 1
    
for i in range(10001):
    if P[i] != 0:
        for j in range(P[i]):
            print(i)