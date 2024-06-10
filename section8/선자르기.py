# 선자르기를 dfs로 풀었더니 시간이 너무 오래걸린당..
n = int(input())  # n미터 짜리 선을 자르는 방법의 가짓수
memo = [0] * (n+1)
memo[0] = 1
memo[-1] = 1
cnt = 0


def dfs(index, value):
    global cnt
    if index == n:
        cnt += 1
        return
    else:  # index < n (1 ~ n-1)
        if value == 0:
            dfs(index+1, 1)
        else:
            dfs(index+1, 0)
            if index+1 != n:
                dfs(index+1, 1)


dfs(0, 1)
print(cnt)