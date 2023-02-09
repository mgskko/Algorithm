n , l = list(map(int, input().split()))
h = list(map(int, input().split()))
h.sort(reverse=False)
for i in range(len(h)):
    if l >= h[i]:
        l += 1
    else:
        break
print(l)