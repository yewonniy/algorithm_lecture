import itertools

n, f = map(int, input().split())
arr = [x for x in range(1, n+1)]
per = list(itertools.permutations(arr, n))
res = [1, 1]
for _ in range(n - 2):
    temp = [x for x in res]
    res = [1]
    for i in range(len(temp)-1):
        res.append(temp[i] + temp[i+1])
    res.append(1)

for arr in per:
    total = 0
    for i in range(n):
        total += arr[i] * res[i]
    if total == f:
        for x in arr:
            print(x, end=' ')
        break