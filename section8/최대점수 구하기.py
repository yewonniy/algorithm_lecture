n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]  # [(점수, 시간) ... ]
dp = [[0] * (m+1) for _ in range(n)]

for i in range(n):
    score = arr[i][0]
    time = arr[i][1]
    for j in range(m+1):
        if j >= time:
            if i == 0:
                dp[i][j] = score
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-time] + score)
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j])
print(max(dp[n-1]))