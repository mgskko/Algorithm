a, b = map(int,input().split())
result = 1
while(a!=b):
  result += 1
  temp = b
  if b % 10 == 1:
    b //= 10
  elif b % 2 == 0:
    b //= 2

  if temp == b:
    print(-1)
    break
else:
  print(result)