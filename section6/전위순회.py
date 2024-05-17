def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=' ')
    for x in graph[start]:
        if not visited[x]:
            dfs(graph, x, visited)


# 인접 리스트
arr = [
    [],
    [2,3],
    [4,5],
    [6,7],
    [2],
    [2],
    [3],
    [3]
]
v = [False] * 8

dfs(arr, 1, v)