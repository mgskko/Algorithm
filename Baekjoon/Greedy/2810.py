A = int(input())
M = input()

count = M.count('LL')

if count <= 1:
    print(len(M))
else:
    print(len(M) - int(count) + 1)
