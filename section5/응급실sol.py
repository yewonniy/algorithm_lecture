from collections import deque
n, m = map(int, input().split())
a = list(map(int, input().split()))
arr = []
for index, x in enumerate(a):
    arr.append([index, x])
q = deque(arr)
cnt = 0

while q:
    cur = q.popleft()
    if any(cur[1] < x[1] for x in q):  # 단 1개라도 참이면 참이됨!! if any 문.. 기억해
        q.append(cur)
    else:
        cnt += 1
        if cur[0] == m:
            break

print(cnt)