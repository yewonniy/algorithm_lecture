# 실패!!! 포기!!!!!

n = int(input())
arr = list(map(int, input().split()))
count = []
maxi = 0
index = 0

for i in range(n):
    cnt = 0
    for j in range(i, n):
        if arr[j] > arr[i]:
            cnt += 1
    count.append(cnt)
    if cnt > maxi:
        maxi = cnt
        index = i

cnt = 0
memo = [-1]
for i in range(index, n-1):
    if count[i] == max(count[i+1:]):
        idx = count[i+1:].index(max(count[i+1:])) + i+1
        if arr[i] > arr[idx] > memo[-1]:
            memo.append(arr[idx])
            cnt += 1
            i = idx
    elif count[i] > max(count[i+1:]) and arr[i] > memo[-1]:
        memo.append(arr[i])
        cnt += 1
        for k in range(i, n):
            if arr[k] <= arr[i]:
                count[k] = -1
if memo[-1] < arr[-1]:
    cnt += 1
    memo.append(arr[-1])
print(memo)
print(cnt)
