# 어떻게 하면 시간을 줄일 수 있을까...
n, m = map(int, input().split())
arr = [i for i in range(1, n + 1)] * m
index = [0] * (n * m + 1)  # 얘가 1이면 해당 값의 인덱스를 선택
result = []


def dfs(level, one_cnt):
    if one_cnt > m:
        return
    if level == (n * m):
        if one_cnt == m:
            a = []
            for i, value in enumerate(index):
                if value == 1:
                    a.append(arr[i])
            if a not in result:
                result.append(a)  # 길이가 m이면 result에 append
    else:
        index[level] = 1
        dfs(level + 1, one_cnt + 1)
        index[level] = 0
        dfs(level + 1, one_cnt)


dfs(0, 0)
result.sort()
for x in result:
    for i in range(len(x)):
        print(x[i], end=' ')
    print()
print(len(result))