n = int(input())
players = [list(map(int, input().split())) for _ in range(n)]
players.sort(reverse=True)  # 키를 기준으로 정렬 (큰 사람이 앞에)
max_weight = 0
cnt = 0

# players[i]가 [0](키)에서는 무조건 i+1보다 작음 [1](몸무게)이 무조건 커야함
# 즉 키가 작은 사람이 cnt 되려면 몸무게가 점점 더 커져야한다.
# 따라서 키 큰 사람부터 내려오면서 첫 사람보다 몸무게가 높은 사람은 다 넣으면 됨
for i in range(n):
    if players[i][1] > max_weight:
        max_weight = players[i][1]
        cnt += 1

print(cnt)