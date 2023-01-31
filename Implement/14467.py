import sys
n = int(sys.stdin.readline())
result = 0
arr = {}

for _ in range(n):
  n1, n2 = map(int, sys.stdin.readline().split())
  if n1 not in arr:
    arr[n1] = n2
  else:
    if arr[n1] != n2:
      result += 1
      arr[n1] = n2
print(result)