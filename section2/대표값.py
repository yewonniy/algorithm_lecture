n = int(input())
scores = list(map(int, input().split()))

average = int((sum(scores) / n) + 0.5)

diff = []
for score in scores:
    diff.append(score - average)

under = -100
over = 100
for num in diff:
    if num < 0:
        if num > under:
            under = num
    else:
        if num < over:
            over = num

if -under < over:
    print(average, diff.index(under)+1)
else:
    print(average, diff.index(over)+1)