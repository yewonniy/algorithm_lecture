n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()


def binary_search(arr, target):
    start = 0
    end = len(arr)
    while True:
        mid_index = (start + end) // 2
        if arr[mid_index] == target:
            break
        elif arr[mid_index] < target:
            start = mid_index
        else:
            end = mid_index
    return mid_index


print(binary_search(arr, m)+1)