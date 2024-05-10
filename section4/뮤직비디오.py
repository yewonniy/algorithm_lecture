n, m = map(int, input().split())  # 곡의 갯수, 비디오의 갯수
arr = list(map(int, input().split()))  # 곡의 길이

result = 0
# 구간 = max(arr) ~ sum(arr)
for capacity in range(max(arr), sum(arr)+1):
    total_length = 0
    cnt = 0
    for i in range(n):
        if total_length + arr[i] > capacity:
            cnt += 1
            # print(capacity,"일때", i,"에서 카운트", cnt)
            total_length = 0 # 다음 비디오를 채움
        if cnt > m:
            break
        total_length += arr[i]
        if i == n-1:
            cnt += 1
    if cnt <= m:
        result = capacity
        break
print(result)