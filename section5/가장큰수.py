# 못 풀었음.. (영상 조금 보고 나서 다시 풀어봄 -> 나보다 작은 놈이 내 앞에 있으면 안된다는 논리!)
# stack을 이용해서 풀면 됨!!! (나보다 작은 놈이 내 앞에 있으면 걜 없애는 아이디어)

a, n = input().split()
n = int(n)
arr = list(map(int, list(a)))  # '12345' -> [1, 2, 3, 4, 5]
result = [arr[0]]


def make_num(remove_cnt):
    for i in range(1, len(arr)):
        if remove_cnt == n:
            return i
        l = len(result)
        for _ in range(l):
            if arr[i] > result[-1]:
                result.pop()
                remove_cnt += 1
                if remove_cnt == n:
                    return i
        result.append(arr[i])
    return -1  # remove_cnt < n (더 잘라내야함)


index = make_num(0)
if len(result) < len(arr)-n:
    for i in range(index, len(arr)):
        result.append(arr[i])
for i in range(len(arr)-n):
    print(result[i], end='')