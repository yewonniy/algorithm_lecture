import itertools

n, k = map(int, input().split())
nums = list(map(int, input().split()))
m = int(input())
arr = [-1] * k
cnt = 0


def dfs(level, index):
    global cnt, arr
    if level == k:
        if sum(arr) % m == 0:
            cnt += 1
    else:
        arr[level] = nums[index]
        if level == k-1:
            dfs(level+1, index)
        else:
            for i in range(index+1, n):
                dfs(level+1, i)


for i in range(0, n-k+1):
    dfs(0, i)

print(cnt)
#[(2, 4, 5), (2, 4, 8), (2, 4, 12), (2, 5, 8), (2, 5, 12),
# (2, 8, 12), (4, 5, 8), (4, 5, 12), (4, 8, 12), (5, 8, 12)]
