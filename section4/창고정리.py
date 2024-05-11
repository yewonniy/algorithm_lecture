l = int(input())
arr = list(map(int, input().split()))
m = int(input())
arr.sort()

for _ in range(m):
    j = 0
    k = 0
    while arr[l - 1 - j] <= arr[l - 2 - j]:
        j += 1
    while arr[k] >= arr[k + 1]:
        k += 1
    arr[l - 1 - j] -= 1
    arr[k] += 1
print(max(arr) - min(arr))