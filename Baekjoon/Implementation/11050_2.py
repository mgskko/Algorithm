n, k = map(int,input().split())

def fa(n):
  if n <= 1:
    return 1
  else:
    return fa(n - 1) * n

print(fa(n) // (fa(k)*fa(n - k)))

