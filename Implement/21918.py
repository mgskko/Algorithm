import sys
n, m = map(int, sys.stdin.readline().split())
s = list(map(int, sys.stdin.readline().split()))

for i in range(m):
  state = list(map(int, sys.stdin.readline().split()))

  if state[0] == 1:
    s[state[1] - 1] = state[2]
  
  elif state[0] == 2:
    for j in range(state[1]-1,state[2]):
      if s[j] == 0:s[j] = 1
      else : s[j] = 0
    
  elif state[0] == 3:
    for j in range(state[1]-1, state[2]):
        if s[j] == 1:
          s[j] = 0 

  elif state[0] == 4:
    for j in range(state[1]-1, state[2]):
        if s[j] == 0:
          s[j] = 1

print(*s)

# 리스트 요소 한번에 출력하기:  print(*arr) 