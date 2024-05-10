n, m = map(int, input().split())  # 곡의 갯수, 비디오의 갯수
arr = list(map(int, input().split()))  # 곡의 길이


# 구간 = max(arr) ~ sum(arr)
def binary(arr, n, m, start, end, res):
    if start > end:
        return res
    capacity = (start + end) // 2  # mid 역할
    total_length = 0
    cnt = 0
    for i in range(n):
        if total_length + arr[i] > capacity:  # 이번 숫자를 더하면 용량을 넘어갈 경우
            cnt += 1
            total_length = 0  # 다음 비디오를 채움
        total_length += arr[i]
        if i == n-1:
            cnt += 1
    if cnt > m:
        return binary(arr, n, m, capacity+1, end, res)  # 용량을 늘려
    if cnt <= m:
        res = capacity
        return binary(arr, n, m, start, capacity-1, res)  # 용량을 줄여


result = binary(arr, n, m, max(arr), sum(arr)+1, -1)
print(result)