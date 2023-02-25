n = input()
a = []

for i in range(len(n)):
    a.append(n[i])
a.sort(reverse=True)
print(''.join(a))
