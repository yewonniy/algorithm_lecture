c, n = map(int, input().split())
w = [int(input()) for _ in range(n)]
result = -1


def dfs(level, total):
    if total > c:
        return
    if level == n:
        global result  # 전역 변수 (global)은 여기에서 선언!!!! 밖에서 선언하지 않는다!!
        result = max(result, total)
    else:
        dfs(level+1, total + w[level])
        dfs(level+1, total)


dfs(0, 0)
print(result)