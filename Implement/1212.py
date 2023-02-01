import sys
n = sys.stdin.readline()
result = []
ans = ''

for i in n:
  for _ in range(3):
    result.append(str(int(i) % 2))
    i = int(i) // 2
  result = result[::-1]
  ans += ''.join(result)
  result = []
print(int(ans))