n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
for i in range(n):
    for j in range(n):
        up = False
        down = False
        left = False
        right = False
        # arr[i][j] 가 봉우리인지 계산해보기
        # 상
        if (i-1 >= 0 and arr[i-1][j] < arr[i][j]) or i-1 < 0:
            up = True
        # 하
        if (i+1 < n and arr[i+1][j] < arr[i][j]) or i+1 >= n:
            down = True
        # 좌
        if (j-1 >= 0 and arr[i][j-1] < arr[i][j]) or j-1 < 0:
            left = True
        # 우
        if (j+1 < n and arr[i][j+1] < arr[i][j]) or j+1 >= n:
            right = True
        if up and down and left and right:
            cnt += 1
print(cnt)