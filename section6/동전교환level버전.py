# 강의 설명 듣고 다시 푼 버전
n = int(input())
coin = list(map(int, input().split()))
coin.sort(reverse=True)
m = int(input())
mini = 2147000000


def dfs(level, total):
    global mini
    if level > mini:  # 이러면 최적의 답이 아니니까 조기 리턴
        return
    if total > m:
        return
    elif total == m:
        mini = min(mini, level) # level이 곧 사용한 동전의 개수가 됨!!
        return
    else:
        for x in coin:
            dfs(level+1, total+x)


dfs(0, 0)
print(mini)