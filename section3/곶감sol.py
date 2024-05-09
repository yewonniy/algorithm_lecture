n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
m = int(input())

# 곶감 돌리기
for i in range(m):
    row, direction, cnt = map(int, input().split())
    row -= 1
    cnt = cnt % n
    if direction == 0:
        for _ in range(cnt):
            arr[row].append(arr[row].pop(0)) # 하.. 이렇게 하면 쉽네......... 맨 앞 원소를 pop해서 맨 뒤에 넣기
    else:
        for _ in range(cnt):
            arr[row].insert(0, arr[row].pop()) # 맨 뒤 원소를 pop해서 0번 인덱스에 insert하기

# 모래시계 모양 개수 구하기
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