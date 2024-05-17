n = int(input())


def dfs(num):
    if num > n:
        return
    else:
        res.append(num)
        dfs(num * 2)  # 왼
        dfs(num * 2 + 1)  # 오


for _ in range(3):
    res = []
    dfs(1)
    n -= 1
    print(res)