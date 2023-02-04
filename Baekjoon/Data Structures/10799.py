import sys
n = int(sys.stdin.readline())
stack = []
for i in range(n):
    word = sys.stdin.readline().split()
    for j in range(len(word)):
        stack.append(word[j])
    print("Case #%d: %s" % (i+1, " ".join(stack[::-1])))
    stack.clear()
