n = int(input())

group_word = 0

for _ in range(n):
  word = input()
  result = 0
  for i in range(len(word)-1):
    if word[i] != word[i+1]:
      new = word[i+1:]
      if new.count(word[i]) > 0:
        result += 1
  if result == 0:  
    group_word += 1
print(group_word)