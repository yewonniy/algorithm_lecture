n = int(input())
arr = []
for _ in range(n):
    area, height, weight = map(int, input().split())
    arr.append([area, weight, height])
arr.sort()

dp = [0] * n
for i in range(n):
    maxi = arr[i][2]
    for j in range(i):
        if arr[j][1] < arr[i][1]:
            maxi = max(maxi, dp[j] + arr[i][2])
    dp[i] = maxi
print(max(dp))