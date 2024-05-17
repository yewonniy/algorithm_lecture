n = int(input())
arr = []
for _ in range(n):
    t, p = map(int, input().split())  # t가 상담 소요 기간, p는 받는 금액
    arr.append([t, p])
res = -1


# 구해야 하는 것 : 총 금액 합계
def dfs(index, total):
    global res
    if index > n:
        return
    elif index == n:
        res = max(res, total)  # 이거!! 안 적어서 답이 안 나왔었음.. dfs 마지막 호출? 이라 해야되나.. 아무튼 마지막 끝 처리 잘하기!!
        return
    else:
        res = max(res, total)
        dfs(index + 1, total)  # 나를 안넣고 다음날 상담
        dfs(index + arr[index][0], total + arr[index][1])  # 나를 넣고 t시간 뒤 상담


dfs(0, 0)
print(res)