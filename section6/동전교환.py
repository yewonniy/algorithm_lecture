# 가장 적은 수의 동전 (개수가 적어야 해)
n = int(input())
coin = list(map(int, input().split()))
coin.sort(reverse=True)
m = int(input())
mini = 1000000000


def dfs(total, cnt):
    global mini
    if cnt > mini:  # 조기 리턴
        return
    if total > m:
        return
    elif total == m:
        mini = min(mini, cnt)
        return
    else:
        # 로직 실행
        for x in coin:
            total += x
            cnt += 1
            dfs(total, cnt)
            total -= x
            cnt -= 1


dfs(0, 0)
print(mini)