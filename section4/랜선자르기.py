import sys
k, n = map(int, input().split())
line = [int(sys.stdin.readline().rstrip()) for _ in range(k)]


def cut(arr, n, maxi, mini):  # n개의 랜선을 만들어야 함
    mid = (mini + maxi) // 2
    cnt = 0
    for x in arr:
        cnt = cnt + (x // mid)
    if maxi - mini < 2:
        return mid
    if cnt < n:  # mid(길이)를 줄여야함 갯수를 늘리기 위해
        return cut(arr, n, mid, mini)
    elif cnt > n:  # mid를 늘려 갯수 줄여
        return cut(arr, n, maxi, mid)
    else:
        return mid


result = cut(line, n, max(line), 0)
while True:
    cnt = 0
    for x in line:
        cnt = cnt + (x // (result + 1))
    if cnt < n:
        break
    result += 1
print(result)