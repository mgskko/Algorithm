n, m = map(int, input().split())
a = set()

for i in range(n):
    a.add(input())

b = set()
for i in range(m):
    b.add(input())

r  = sorted(list(a & b))
print(len(r))

for i in r:
    print(i)