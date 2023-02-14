t = int(input())


def fa(n):
  if n <= 1:
    return 1
  else:
    return fa(n - 1) * n

for _ in range(t):
  n, m = map(int,input().split())
  print(fa(m) // (fa(n)*fa(m - n)))