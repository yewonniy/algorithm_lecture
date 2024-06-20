n, w = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (w+1)  # dp[i] = i 무게가 베낭의 최대 무게일 때 담을 수 있는 보석의 최대 가치

for i in range(n):
    for j in range(w+1):
        index = j - arr[i][0]
        if index >= 0:
            dp[j] = max(dp[j], dp[index] + arr[i][1])  # 기존 값보다 크면 바꿔준다!!!
    print(dp)
print(dp[w])