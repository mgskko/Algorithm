M = [1 , 2, 3, 4, 5]
num = 0
for i in range(5):
        for j in range(i + 1):
                print(j)
                num += M[j]
print(num)

for i in range(1):
        print(i,"d")