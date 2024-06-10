m, n = map(int, input().split())
cnt = 0


def print_list(result):
    for x in result:
        print(x, end=' ')
    print()


def dfs(num):
    result.append(num)
    if not check[num]:
        check[num] = True
    else:
        return
    if len(result) == n:
        print_list(result)
        global cnt
        cnt += 1
        return
    for i in range(1, m+1):
        dfs(i)
        if len(result) > 1:
            pop = result.pop()
            if pop not in result:
                check[pop] = False


for i in range(1, m+1):
    result = []  # len(result) == n 이면 끝
    check = [False] * (m + 1)  # false 면 사용 안한거. True면 사용한 거
    dfs(i)
print(cnt)