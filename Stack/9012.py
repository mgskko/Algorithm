import sys
N = int(sys.stdin.readline())

for i in range(N):
    stack = []
    word = sys.stdin.readline()
    for j in word:
        if j == "(":
            stack.append(j)
        elif j == ")":
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if not stack:
            print('YES')
        else:
            print("NO")
