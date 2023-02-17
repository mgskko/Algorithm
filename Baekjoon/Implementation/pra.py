a = input()
k = []
for i in a:
    k.append(i)    
k.sort(reverse=True)
print("".join(k))