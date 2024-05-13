# queue를 이용해서 푼 버전!! (원형으로 도는 논리 -> 앞부분을 팝해서 뒤로 넣는다)
from collections import deque
n, k = map(int, input().split())
queue = deque()
for i in range(1, n+1):
    queue.append(i)
# queue = deque(list(range(1, n+1))

for _ in range(n-1):
    for _ in range(k-1):
        queue.append(queue.popleft())
    queue.popleft()
print(queue[0])