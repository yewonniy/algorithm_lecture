# 나의 역작이다..
n = int(input())
score = [0] * n
arr = list(map(int, input().split()))

for index in range(n):
    if arr[0] == 1:
        score[0] = 1
    if arr[index] == 1 and index > 0:
        score[index] = score[index-1] + 1
print(sum(score))