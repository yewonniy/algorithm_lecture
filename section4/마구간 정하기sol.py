n, horse = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()


def distance(arr, start, target):
    for i in range(start+1, len(arr)):
        if arr[i] - arr[start] >= target:
            return i
    return -1


def binary(arr, start, end, res):
    if start > end:
        return res
    mid = (start + end) // 2
    s = 0
    for i in range(horse-1):
        now = distance(arr, s, mid)  # now는 인덱스
        if now == -1:  # mid를 작게 해야 함
            return binary(arr, start, mid-1, res)
        s = now
    res = mid
    return binary(arr, mid+1, end, res)


result = binary(arr, 1, arr[n-1], -1)
print(result)