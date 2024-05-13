n, k = map(int, input().split())
arr = [0 for _ in range(n)]

i = -1
for _ in range(n-1):  # n-1명을 제거해야하니까
    for _ in range(k):
        i += 1
        if i > n-1:
            i = i % n
        while arr[i] == 1:
            i += 1
            if i > n-1:
                i = i % n
    arr[i] = 1

print(arr.index(0) + 1)