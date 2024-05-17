# 중복이 허용되지 않음.. n 개 중 m개 뽑기 그 자체;
n, m = map(int, input().split())
arr = [i for i in range(1, n + 1)] * m
print(arr)
result = []


def dfs(level, one_cnt):
    if level == n + 1:
        if one_cnt == m:
            a = []
            for i in range(n + 1):
                if arr[i] == 1:
                    a.append(i)
            result.append(a)  # 길이가 m이면 result에 append
    else:
        arr[level] = 1
        dfs(level + 1, one_cnt + 1)
        arr[level] = 0
        dfs(level + 1, one_cnt)


dfs(1, 0)
print(result)