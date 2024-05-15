import heapq
a = []
res = []

while True:
    n = int(input())
    if n == -1:
        break
    elif n == 0:
        res.append(-heapq.heappop(a))
    else:
        heapq.heappush(a, -n)

print(res)
for x in res:
    n = int(input())
    if x != n:
        print("False")
        break
else:
    print("True")