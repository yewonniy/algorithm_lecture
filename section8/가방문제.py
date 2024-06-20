n, w = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort()  # 무게를 기준으로 정렬 (가벼운 거 -> 무거운 거)

dp = [0] * (w+1)  # dp[i] = i 무게가 베낭의 최대 무게일 때 담을 수 있는 보석의 최대 가치
dp[arr[0][0]] = arr[0][1]

for i in range(arr[0][0]+1, w+1):
    maxi = 0
    for j in range(n):
        index = i - arr[j][0]
        if index < 0:
            break
        maxi = max(dp[index] + arr[j][1], maxi)
    dp[i] = maxi

print(dp[w])