n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
arr.sort(reverse=True)


# 일찍 시작하는 걸 기준으로 정렬해서 선택했음!! -> 근데 빨리 끝나는 걸 기준으로 정렬해서도 할 수 있음!!
def cal(arr):
    new = [arr[0]]
    j = 0
    for i in range(1, len(arr)):
        if new[j][0] >= arr[i][1]:
            new.append(arr[i])
            j += 1
    return new


result = cal(arr)
print(len(result))