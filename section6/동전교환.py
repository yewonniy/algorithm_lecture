import sys
sys.setrecursionlimit(1000000)
# 가장 적은 수의 동전 (개수가 적어야 해)
n = int(input())
coin = list(map(int, input().split()))
money = int(input())
mini = 1000000000


# coin 안에 들어있는 숫자를 잘 조합해 sum이 money가 되게 하는 가장 작은 원소 수를 구해라
def dfs(v, total, cnt):
    global mini
    if v == n or total > money or cnt > mini:
        return
    if total == money:
        mini = min(mini, cnt)
    else:
        total += coin[v]
        dfs(v, total, cnt+1)
        if v+1 < n:
            total = total - coin[v] + coin[v+1]
            dfs(v+1, total+coin[v+1], cnt+1)


dfs(0, 0, 0)
print(mini)