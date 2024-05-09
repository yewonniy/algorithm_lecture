def success(sdocu):
    # 가로
    for row in sdocu:
        for num in range(1, 10):
            if row.count(num) != 1:
                return "NO"
    # 세로
    for i in range(9):
        column = []
        for j in range(9):
            if column.count(sdocu[j][i]) > 0:  # 이미 있으면
                return "No"
            else:  # 없으면
                column.append(sdocu[j][i])
    # 사각형
    for k in range(3):
        i = 0
        for _ in range(3):
            square = []
            for _ in range(3):
                j = k * 3
                for _ in range(3):
                    if square.count(sdocu[i][j]) > 0:
                        return "No"
                    else:
                        square.append(sdocu[i][j])
                    j += 1
                i += 1
    return "YES"


s = [list(map(int, input().split())) for _ in range(9)]
print(success(s))