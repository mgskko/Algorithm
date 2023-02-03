a = input().split('-')
c = 0
for i in a[0].split('+'):
    c += int(i)
for i in a[1:]:
    for j in i.split('+'):
        c -= int(j)
print(c)
