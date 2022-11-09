N = input()
n = []
for i in range(len(N)):
    n += N[i]
n.sort(reverse=True)
print(''.join(n))
