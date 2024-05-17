c, n = map(int, input().split())
result = -2147000000
w = [int(input()) for _ in range(n)]
total = sum(w)


def dfs(l, sum, tsum):
    global result
    if sum + (total - tsum) < result:  # 중요 중요!!!!!!!!! 시간 복잡도를 낮추는 키포인트
        return
    if sum > c:
        return
    if l == n:
        if sum > result:
            result = sum
    else:
        dfs(l + 1, sum + w[l], tsum + w[l])
        dfs(l + 1, sum, tsum + w[l])


dfs(0, 0, 0)
print(result)
