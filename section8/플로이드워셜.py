n, m = map(int, input().split())  # 도시 수, 간선 수
arr = [list(map(int, input().split())) for _ in range(m)]  # [[도시1, 도시2, 비용], []...]

dis = [[float("inf")] * n for _ in range(n)]
for i in range(n):
    dis[i][i] = 0
for i in range(m):
    dis[arr[i][0]-1][arr[i][1]-1] = arr[i][2]
for k in range(n):
    for i in range(n):
        for j in range(n):
            dis[i][j] = min(dis[i][k] + dis[k][j], dis[i][j])

for x in dis:
    print(x)