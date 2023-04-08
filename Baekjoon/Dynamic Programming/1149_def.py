def calculate_min_cost(n, rgb):
    for i in range(1,n):
        rgb[i][0] = rgb[i][0] + min(rgb[i-1][1],rgb[i-1][2])
        rgb[i][1] = rgb[i][1] + min(rgb[i-1][0],rgb[i-1][2])
        rgb[i][2] = rgb[i][2] + min(rgb[i-1][1],rgb[i-1][0])
    return min(rgb[n-1])

n = int(input())
rgb = []
for i in range(n):
    a,b,c = map(int,input().split())
    rgb.append([a,b,c])

print(calculate_min_cost(n, rgb))
