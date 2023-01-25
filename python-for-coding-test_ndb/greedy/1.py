n = 1260
k = [500, 100, 50, 10]
c = 0
for i in k:
    c += n // i
    n %= i

print(c)
