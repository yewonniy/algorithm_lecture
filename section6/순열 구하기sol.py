def dfs(l):
    global cnt
    if l == m:
        for j in range(l):
            print(res[j], end=' ')
        print()
        cnt += 1
    else:
        for i in range(1, n+1):
            if not check[i]:
                check[i] = True
                res[l] = i
                dfs(l+1)
                check[i] = False  # 호출 위 아래는 대칭!!!!!!


n, m = map(int, input().split())
res = [0] * n
check = [False] * (n+1)
cnt = 0
dfs(0)