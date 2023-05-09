import sys
input = sys.stdin.readline

# 원생 수와 제거할 원생 수를 입력받습니다.
n, k = map(int, input().split())

# 원생들의 키 정보를 리스트로 입력받습니다.
kids = list(map(int, input().split()))

# 인접한 원생과의 키 차이를 계산하여 리스트에 저장합니다.
diff = [kids[i+1] - kids[i] for i in range(n-1)]

# 키 차이를 오름차순으로 정렬합니다.
diff.sort()

# 제거할 원생 수(n-k)만큼 키 차이의 합을 계산하여 출력합니다.
print(sum(diff[0:n-k]))
