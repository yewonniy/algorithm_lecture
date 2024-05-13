from collections import deque
n, m = map(int, input().split())
a = list(map(int, input().split()))
arr = []
for index, x in enumerate(a):
    arr.append([index, x])
q = deque(arr)
cnt = 0

while q:
    for j in range(len(q)):
        if q[0][1] < q[j][1]:
            q.append(q.popleft())
            break
    else:
        cur = q.popleft()
        cnt += 1
        if cur == arr[m]:
            print(cnt)
            break