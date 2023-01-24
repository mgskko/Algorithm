t = int(input())
c = []
q = [25, 10, 5, 1]
d = [0] * 4

for i in range(t):
    c.append(int(input()))

    for j in range(len(q)):
        d[j] = c[i] // q[j]
        c[i] = c[i] % q[j]
    print(' '.join(map(str, d)))
