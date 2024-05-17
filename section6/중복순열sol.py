# 미쳤다.. ㅋㅋ 상태 트리 잘 생각하기!!!!!! 트리가 여러 가닥으로 뻗음!! 이진트리가 아님
n, m = map(int, input().split())
res = [0] * m
cnt = 0


def dfs(level):
    global cnt
    if level == m:
        cnt += 1
        for x in res:
            print(x, end=' ')
        print()
        return
    else:
        for i in range(1, n+1): # 1부터 n까지
            res[level] = i  # 생각의 전환!!
            dfs(level+1)


dfs(0)
print(cnt)