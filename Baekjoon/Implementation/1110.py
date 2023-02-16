n = input()

if(int(n) < 10):
    n = '0' + n
    
check_value = int(n)
cnt = 0
while True:
    add_value = int(n[0]) + int(n[1])
    cnt += 1

    n = n[-1] + str(add_value)[-1]
    if(check_value == int(n)):
        break
        
print(cnt)