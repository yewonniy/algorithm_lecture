from collections import deque
n, m = map(int, input().split())
w = list(map(int, input().split()))
w.sort()
weight = deque(w)  # list는 pop(0)을 하면 1번째 원소부터 앞으로 한 칸씩 민다!! -> 비효율적, so deque (큐) 사용!!

cnt = 0
while weight:
    if weight[0] + weight[-1] <= m and len(weight) > 1:
        cnt += 1
        weight.popleft()
        weight.pop()
    else:  # 맨 뒷 사람은 무조건 혼자 타야함
        cnt += 1
        weight.pop()
print(cnt)
