# 바텀업 방식!!!

n = int(input())
arr = []
dp = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
    dp.append([0] * n)
dp[0][0] = arr[0][0]

for i in range(n):
    for j in range(n):
        if i == 0:
            if j > 0:
                dp[i][j] = dp[i][j-1] + arr[i][j]
        else:
            if j == 0:
                dp[i][j] = dp[i-1][j] + arr[i][j]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + arr[i][j]
print(dp[n-1][n-1])


# 탑다운 방식 => 재귀
memo = [[0] * n for _ in range(n)]


def dfs(x, y):
    if memo[x][y] > 0:
        return memo[x][y]
    if x == 0 and y == 0:
        return arr[0][0]
    else:
        if y == 0:
            memo[x][y] = dfs(x-1, y) + arr[x][y]
        elif x == 0:
            memo[x][y] = dfs(x, y-1) + arr[x][y]
        else:
            memo[x][y] = min(dfs(x-1, y), dfs(x, y-1)) + arr[x][y]
        return memo[x][y]