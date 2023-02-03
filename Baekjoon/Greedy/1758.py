import sys
n = int(sys.stdin.readline())
tips = []
result = 0
for i in range(n):
  tips.append(int(sys.stdin.readline()))

tips.sort(reverse=True)

for tip in range(n):
  value = (tips[tip]-(tip))
  if value > 0:
    result += value
print(result)