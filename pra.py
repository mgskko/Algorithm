import sys
input = sys.stdin.readline
n = int(input())
t = list(map(int, input().split()))
t.sort()
cnt = 0
k = []
if (len(t) % 2) == 1:
    k.append(t.pop(-1))
for i in range(len(t)):
    if t[i] > t[(len(t)-i-1)]:
        break
    k.append(t[i]+t[(len(t)-i-1)])
    
print(max(k))
