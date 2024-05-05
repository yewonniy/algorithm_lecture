# 아.. 인덱스 번호를 합의 결과로 생각하기
# 합의 결과에 해당하는 인덱스를 + 1 한다

n, m = map(int, input().split())
cnt = [0] * (n + m + 1)

for i in range(1, n+1):
    for j in range(1, m+1):
        cnt[i+j] += 1 # 여기가 핵심!

maxi = max(cnt)
for index, x in enumerate(cnt):
    if x == maxi:
        print(index, end=' ')