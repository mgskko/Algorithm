while True:
  x=input()
  if x == '0':
    break
  if len(x) % 2 == 1:
    if  x[:int(len(x)/2):-1] == x[0:int(len(x)/2)]:
      print('yes')
    else:
      print('no')
  elif len(x) % 2 == 0:
    if  x[:int(len(x)/2)-1:-1] == x[0:int(len(x)/2)]:
      print('yes')
    else:
      print('no')
