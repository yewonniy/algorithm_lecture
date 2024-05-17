import sys


def dfs(level, sum):  # level = index와 비슷한 의미
    if sum * 2 > total:
        return
    if level == n:
        if sum == total - sum:
            print("YES")
            sys.exit(0)
    else:
        dfs(level+1, sum+a[level])
        dfs(level+1, sum)


n = int(input())
a = list(map(int, input().split()))
total = sum(a)
dfs(0, 0)