n = int(input())
arr = list(map(int, input().split()))
result = [0 for _ in range(n)]  # [0] * n

for i in range(n):
    count_zero = 0
    for j in range(n):
        if result[j] == 0:
            count_zero += 1
        if count_zero == arr[i] + 1:
            result[j] = i+1
            break

for num in result:
    print(num, end=' ')