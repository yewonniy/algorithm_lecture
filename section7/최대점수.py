n, m = map(int, input().split())  # m이 time limit
arr = []
for _ in range(n):
    score, time = map(int, input().split())
    arr.append([score, time])
maxi = -1


# 구해야 하는 것: 점수 총합, 시간 총합
def dfs(level, score, time):
    global maxi
    if level == n:
        return
    if time > m:
        return
    else:  # time <= m
        maxi = max(maxi, score)
        dfs(level+1, score, time)
        dfs(level+1, score + arr[level][0], time + arr[level][1])


dfs(-1, 0, 0)
print(maxi)