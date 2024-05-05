def digit_sum(num):
    result = 0
    while num > 0:
        result += num % 10
        num = num // 10
    return result


n = int(input())
arr = list(map(int, input().split()))
sum_arr = []
for num in arr:
    sum_arr.append(digit_sum(num))

maxi = max(sum_arr)
for index, num in enumerate(sum_arr):
    if num == maxi:
        print(arr[index], end=' ')