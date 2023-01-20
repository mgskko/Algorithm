import sys
N = int(sys.stdin.readline())
temp = 1
result = 0

while True:
    N -= temp
    if N >= 0:
        temp += 1
        result += 1
    else:
        break
print(result)
