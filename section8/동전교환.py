n = int(input())
arr = list(map(int, input().split()))
m = int(input())
dp = [501] * (m+1)
dp[0] = 0

for i in range(n):
    coin = arr[i]
    for j in range(m+1):
        if j - coin >= 0:
            dp[j] = min(dp[j], dp[j-coin] + 1)
print(dp[m])