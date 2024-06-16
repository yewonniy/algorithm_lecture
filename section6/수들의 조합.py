import itertools

n, k = map(int, input().split())
num = list(map(int, input().split()))
m = int(input())

arr = list(itertools.combinations(num, k))
cnt = 0
for x in arr:
    if sum(x) % m == 0:
        cnt += 1
print(cnt)