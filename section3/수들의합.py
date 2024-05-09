n, m = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
if sum(arr) >= m:
    for i in range(len(arr)):
        sum = 0
        pointer = 0
        for pointer in range(i, len(arr)):
            if sum >= m:
                break
            else:
                sum += arr[pointer]
        if sum == m:
            cnt += 1
            if pointer == len(arr) - 1:
                # 마지막 원소까지 다 더한 게 M과 같으면 더 진행할 필요 X, 앞으로의 합들은 다 M보다 작을 것이므로
                break

print(cnt)
