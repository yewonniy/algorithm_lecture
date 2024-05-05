def cal_price(arr):
    cnt = []
    for n in arr:
        cnt.append(arr.count(n))
    if max(cnt) == 1:
        return max(arr) * 100
    elif max(cnt) == 2:
        return 1000 + arr[cnt.index(2)] * 100
    else:
        return 10000 + arr[0] * 1000


n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

result = -1
for numbers in arr:
    result = max(result, cal_price(numbers))
print(result)