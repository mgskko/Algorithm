import sys
N = int(sys.stdin.readline())
stack = []
for i in range(N):
    word = sys.stdin.readline()
    for j in word:
        if j == "(":
            stack.append(j)
        elif j == ")":
            stack.pop()
    if stack == "":
        print('YES')
    else:
        print("NO")
