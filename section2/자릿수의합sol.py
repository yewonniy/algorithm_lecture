def digit_sum(num):
    result = 0
    for i in str(num): # 123을 '1', '2', '3' 이렇게 하나씩 접근하는 법..!!!!!
        result += int(i)
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