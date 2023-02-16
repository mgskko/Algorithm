n = str(input())
m = n
c = 0
while True:
    if int(n) < 10:
        n = '0'+ n
        c += 1
    k = int(n[0]) + int(n[-1])
    k = str(k)
    k = int(n[-1]) + int(k[-1])
    k = str(k)
    c += 1
    if (n == k):
        break
print(c)