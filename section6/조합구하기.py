# 1부터 n까지 구슬 중 m 개 뽑는 방법의 수
n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]
cnt = 0
res = [0] * m


def dfs(level, num):
    global cnt
    if level == m:
        print(res)
        cnt += 1
    else:
        for i in range(num+1, n+1):
            res[level] = i
            dfs(level+1, i)


dfs(0, 0)
print(cnt)