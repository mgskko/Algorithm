import sys
input = sys.stdin.readline
n, k = map(int, input().split())
ch = list(map(int,input().split()))

ch.sort()
diff = []
for i in range(n-1):
    diff.append(ch[i+1] - ch[i])
diff.sort()
print(sum(diff[:n-k]))