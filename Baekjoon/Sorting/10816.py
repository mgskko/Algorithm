from collections import Counter
import sys

input = sys.stdin.readline

n = int(input())
n1 = list(map(int,input().split()))
m = int(input())
m1 = list(map(int,input().split()))
t = []

count_n1 = Counter(n1)

for i in m1:
    t.append(count_n1[i])

print(*t)