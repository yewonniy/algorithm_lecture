# 길이가 가장 긴 증가 수열 찾기
n = int(input())
arr = list(map(int, input().split()))
dp = [0] * n

for now in range(n):
    maxi = 1
    for j in range(0, now):
        if arr[j] < arr[now]:
            maxi = max(maxi, dp[j]+1)
    dp[now] = maxi
print(max(dp))


# 합이 가장 큰 증가 수열 찾기
# n = int(input())
# arr = list(map(int, input().split()))
# dp = [0] * n

for now in range(n):
    maxi = arr[now]
    for j in range(0, now):
        if arr[j] < arr[now]:
            maxi = max(maxi, dp[j]+arr[now])
    dp[now] = maxi
print(max(dp))