n = int(input())
arr = list(map(int, input().split()))
dp = [0] * n

for i in range(n):
    maxi = 1
    for j in range(i):
        if arr[j] < arr[i]:
            maxi = max(maxi, dp[j] + 1)
    dp[i] = maxi

print(max(dp))