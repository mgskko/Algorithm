N = input()
sum = 0

if "0" not in N:
    print(-1)

else:
    for i in range(len(N)):
        sum += int(N[i])

    if (sum % 3) != 0:
        print(-1)

    else:
        sort_N = sorted(N, reverse=True)
        a = "".join(sort_N)
        print(a)
