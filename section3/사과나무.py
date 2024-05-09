n = int(input())
tree = [list(map(int, input().split())) for _ in range(n)]

apple = 0
start = -1 # 도는 횟수
column = n // 2 + 1 # 인덱스 시작점
for row in range(n):
    if row <= n // 2:  # 행이 절반 이하면 인덱스 시작점이 점점 -1
        start += 2
        column -= 1
        j = column
        for _ in range(start):
            apple += tree[row][j]
            j += 1
    else:
        start -= 2
        column += 1 # 인덱스 시작점이 뒤로 밀려남
        j = column
        for _ in range(start):
            apple += tree[row][j]
            j += 1
print(apple)
