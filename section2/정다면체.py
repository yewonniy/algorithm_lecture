n, m = map(int, input().split())

memo = []
for i in range(1, n+1):
    for j in range(1, m+1):
        memo.append(i + j)

count = []
for num in memo:
    cnt = memo.count(num)
    count.append(cnt)

maxi = max(count)
result = set()
for index, num in enumerate(count):
    if num == maxi:
        result.add(memo[index])

(list(result)).sort()
for x in result:
    print(x, end=' ')
