import sys

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
k = int(sys.stdin.readline())
cnt = 0
left = 0
right = n - 1
a.sort()

while left != right:
  if a[left] + a[right] == k:
    cnt += 1
    left += 1
  elif a[left] + a[right] > k:
    right -= 1
  else:
    left += 1
print(cnt)