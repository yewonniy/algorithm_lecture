# tlqkf...
n = int(input())
memo = [[1, 1, 1], [1, 2], [2, 1]]
count = [0, 1, 2, 3]  # ,5,8,13,21]

for i in range(4, n + 1):
    cnt = 0
    if i % 2 == 0:
        cnt += 1  # [2,2,2..2] 의 경우
    for x in memo:
        len(x)
    count.append(cnt)

print(count[n])
