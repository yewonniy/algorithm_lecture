n, m = map(int, input().split())  # m 시간 안에 최대 점수
arr = []
for _ in range(n):
    score, time = map(int, input().split())
    arr.append([score, time])
maxi = -1


def dfs(index, total_time, total_score):
    global maxi
    if index == n:
        if total_time <= m:
            maxi = max(maxi, total_score)
        return
    else:
        if total_time > m:
            maxi = max(maxi, total_score - arr[index - 1][0])
            return
        else:
            dfs(index + 1, total_time, total_score)
            dfs(index + 1, total_time + arr[index][1], total_score + arr[index][0])


dfs(0, 0, 0)
print(maxi)