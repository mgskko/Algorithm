n = 'happpy'

for i in range(len(n)):
  if n[i] != n[i+1]:
      new = n[i+1:]
  print(new)