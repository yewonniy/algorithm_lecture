n = int(input())
arr = list(map(int, input().split()))
check = [[x, 0] for x in arr]
result = []


def dfs(index):
    if len(result) > 0:
        return  # 더 빠르게 하려고
    if index == n:
        # 출력
        sum1 = 0
        sum2 = 0
        for num, ch in check:
            if ch == 0:
                sum1 += num
            else:
                sum2 += num
        if sum1 == sum2:
            result.append(True)
            return
    else:
        # v 포함
        check[index][1] = 1
        dfs(index+1)
        # 불포함
        check[index][1] = 0
        dfs(index+1)


dfs(0)
if len(result) > 0:
    print("YES")
else:
    print("NO")