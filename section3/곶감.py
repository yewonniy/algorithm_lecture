n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
m = int(input())

for i in range(m):
    row, direction, cnt = map(int, input().split())
    row -= 1
    cnt = cnt % n
    if direction == 1:
        cnt = -cnt
    new = []
    for _ in range(n):
        new.append(arr[row][cnt])
        if cnt == -1 or cnt == n-1: # 오른쪽으로 미는 경우 전자 적용, 왼쪽으로 미는 경우 후자 적용
            cnt = 0
        else:
            cnt += 1
    arr[row], new = new, arr[row]


repeat_cnt = n
index = 0
sum = 0
for i in range(n):
    k = index
    for j in range(repeat_cnt):
        sum += arr[i][k]
        k += 1
    if i < n // 2:
        repeat_cnt -= 2
        index += 1
    else:
        repeat_cnt += 2
        index -= 1
print(sum)