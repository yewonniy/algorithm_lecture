arr = [list(map(int, input().split())) for _ in range(7)]

# 회문 검사하는 함수
def palindrome(arr):
    for i in range(5):
        if arr[i] != arr[4-i]:
            return False
    return True


cnt = 0
# 가로
for i in range(7):
    for j in range(3):
        if palindrome(arr[i][j: 5+j]):
            cnt += 1
# 세로 (0,0 1,0 2,0 .. 4,0)
for i in range(7):
    for k in range(3):
        new = []
        for j in range(k, 5+k):
            new.append(arr[j][i])
        if palindrome(new):
            cnt += 1
print(cnt)