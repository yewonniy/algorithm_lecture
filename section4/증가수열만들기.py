from collections import deque


def increase_arr(arr, res, prev):
    while arr:
        if arr[0] > prev:
            if arr[0] < arr[-1] or (arr[0] > arr[-1] and arr[-1] < prev):
                res += "L"
                prev = arr.popleft()
        if arr[-1] > prev:
            if arr[-1] < arr[0] or (arr[-1] > arr[0] and arr[0] < prev):
                res += "R"
                prev = arr.pop()
        if arr[0] < prev and arr[-1] < prev:
            return res
    return res


n = int(input())
queue = deque(map(int, input().split()))
result = ""

if queue[0] < queue[-1]:
    result += "L"
    prev = queue.popleft()
else:
    result += "R"
    prev = queue.pop()

result = increase_arr(queue, result, prev)
print(len(result))
print(result)