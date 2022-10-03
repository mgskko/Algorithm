x = int(input())
num = []


for i in range(0,x):
    y = int(input())
    num.append(y)

num.sort()
for i in num:
    print(i)