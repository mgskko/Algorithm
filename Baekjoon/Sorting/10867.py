n = int(input())
t = list(map(int, input().split()))
t = set(t)
t = sorted(t)  # 중복 제거 후 오름차순으로 정렬
print(*t)