n = input()
m = list(0 for _ in range(10))

for i in n:
    num = int(i)
    if num == 6 or num == 9:
        if m[6] <= m[9]:
            m[6] += 1
        else:
            m[9] += 1
    else:
        m[num] += 1
print(max(m))