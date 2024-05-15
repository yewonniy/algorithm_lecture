# heapq 임포트해서 쓴 버전
import heapq
a = []
res = [] # 정답 확인할라고

while True:
    n = int(input())
    if n == -1:
        break
    elif n == 0:
        res.append(heapq.heappop(a))
    else:
        heapq.heappush(a, n)

for x in res:
    if x != int(input()):
        print("False")
        break
else:
    print("True")