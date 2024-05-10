n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()


def binary_search(arr, target, start, end):
    mid = (start + end) // 2
    if start > end:  # target이 arr에 없는 경우!
        return -1
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:  # target이 더 커
        return binary_search(arr, target, mid + 1, end)
    else:
        return binary_search(arr, target, start, mid - 1)


result = binary_search(a, m, 0, n - 1)
if result == -1:
    print("해당 수 없음")
else:
    print(result + 1)
