n = int(input())
players = [list(map(int, input().split())) for _ in range(n)]
players.sort()  # 키를 기준으로 정렬
cnt = 0

for i in range(n - 1):
    if players[i][1] < players[i + 1][1]:  # players[i]가 [0](키)에서는 무조건 i+1보다 작음 [1](몸무게)이 무조건 커야함
        continue
    else:
        for j in range(i + 1, n):  # 이런 범위 잘 설정하자; 맨 처음에 i+2로 해서 실패함 으이구!!!!
            if players[i][1] < players[j][1]:
                break
            if j == n - 1:
                cnt += 1
print(cnt + 1)  # 맨 마지막 선수는 키가 제일 크니까 몸무게가 몇이든 무조건.. 들어감
