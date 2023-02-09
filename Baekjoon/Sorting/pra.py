n, m = list(map(int,input().split()))
n_list = list(map(int,input().split()))
m_list = list(map(int,input().split()))

l = n_list+m_list
l.sort(reverse=False)
print(*l)