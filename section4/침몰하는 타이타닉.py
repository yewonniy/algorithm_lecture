n, m = map(int, input().split())
weight = list(map(int, input().split()))
weight.sort()

cnt = 0
while weight:
    if weight[0] + weight[len(weight) - 1] <= m and len(weight) > 1:
        cnt += 1
        weight.pop(0)
        weight.pop(len(weight) - 1)
    else:  # 맨 뒷 사람은 무조건 혼자 타야함
        cnt += 1
        weight.pop(len(weight) - 1)
print(cnt)
