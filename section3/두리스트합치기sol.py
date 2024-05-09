# (sort()를 사용한 경우 시간 복잡도가 너무 높음)
n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

new = []
i = 0
j = 0
while True:
    if i == len(arr1) and j == len(arr2):
        break
    elif i == len(arr1):
        new.append(arr2[j])
        j += 1
    elif j == len(arr2):
        new.append(arr1[i])
        i += 1
    else:
        if arr1[i] <= arr2[j]:
            new.append(arr1[i])
            if i < len(arr1):
                i += 1
        else:
            new.append(arr2[j])
            if j < len(arr2)-1:
                j +=1
print(new)