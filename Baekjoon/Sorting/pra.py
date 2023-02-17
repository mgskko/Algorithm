n = int(input())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

k = 0

a.sort(reverse=True)
b.sort(reverse=False)
for i in range(n):
    k += a[i] * b[i]
print(k)