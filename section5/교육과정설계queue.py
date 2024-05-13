# queue를 이용한 버전
from collections import deque
m = list(input())
n = int(input())
q = deque()
for _ in range(n):
    q.append(deque(list(input())))

for i in range(n):
    no = False
    subjects = q[i]
    must = deque(list(x for x in m))
    while subjects:
        if subjects[0] in must:
            if subjects[0] == must[0]:
                must.popleft()
                subjects.popleft()
            else:  # 순서 어김
                no = True
                break
        else:
            subjects.popleft()
    if must or no:
        print("NO")
    else:
        print("YES")