n = int(input())
board = []
row_sum = 0
# board = [list(map(int, input().split())) for _ in range(n)] 이렇게도 가능
for _ in range(n):
    low = list(map(int, input().split()))
    board.append(low)
    row_sum = max(row_sum, sum(low))
    # row_sum에는 행의 최대합 들어있음

#column 최대합
column_sum = 0
for column in range(n):
    sum = 0
    for row in range(n):
        sum += board[row][column]
    column_sum = max(column_sum, sum)

# 대각선 최대합
sum1 = 0
sum2 = 0
for i in range(n):
    sum1 += board[i][i]
    sum2 += board[i][n-1-i]
print(max(sum1, row_sum, column_sum, sum2))