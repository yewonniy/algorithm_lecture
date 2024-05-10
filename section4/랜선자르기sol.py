import sys
sys.setrecursionlimit(100000)
k, n = map(int, input().split())
line = [int(sys.stdin.readline().rstrip()) for _ in range(k)]


def cut(arr, target, start, end, res):  # target = 만들어야하는 개수
    if start > end:  # 이 개념을 꼭 명심하기⭐
        return res
    mid = (start + end) // 2
    cnt = 0
    for x in arr:
        cnt = cnt + (x // mid)
    if cnt < target:  # 길이를 줄여! 갯수 늘려
        return cut(arr, target, start, mid-1, res)
    else:  # cnt >= target
        res = mid # 이런 아이디어!!!!!!!!!⭐
        return cut(arr, target, mid+1, end, res)


result = cut(line, n, 1, max(line), 0)
print(result)