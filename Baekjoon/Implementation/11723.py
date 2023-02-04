import sys

m = int(sys.stdin.readline())
s = set()
for _ in range(m):
  com = sys.stdin.readline().split()
  
  if len(com) == 1:
    com0 = com[0]
  else:
    com0, com1 = com

  if com0 == "add":
    s.add(int(com1))
    
  elif com0 == "remove":
    if int(com1) in s:
      s.remove(int(com1))
  
  elif com0 == "check":
    if int(com1) in s:
      print(1)
    else:
      print(0)

  elif com0 == "toggle":
    if int(com1) in s:
      s.remove(int(com1))
    else:
      s.add(int(com1))

  elif com0 == "all":
    s = {1,2,3,4,5,6,7,8,9,10,
             11,12,13,14,15,16,17,18,19,20}

  else:
    s.clear()