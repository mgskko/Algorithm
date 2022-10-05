N = input()
num = []
for i in range(len(N)):
    num += N[i]
num.sort(reverse=True)
print(''.join(num))