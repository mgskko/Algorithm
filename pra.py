import sys
input = sys.stdin.readline
rgb = []
n = int(input())
for i in range(n):
    rgb.append(list(map(int,input().split())))

print(rgb)