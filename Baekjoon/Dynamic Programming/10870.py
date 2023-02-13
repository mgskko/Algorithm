def fi(n):
    if n <= 1:
        return n
    else:
        return fi(n-1) + fi(n-2)

s = int(input())
print(fi(s))