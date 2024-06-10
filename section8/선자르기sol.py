# 와 진짜 바보야.. 제발 이상한 수학하지 말고 규칙을 생각해!!
n = int(input())
count = [0, 1, 2, 3]  # ,5,8,13,21]

for i in range(4, n+1):
    count.append(count[-1] + count[-2])

print(count[n])

dy = [0] * (n+1)
dy[1] = 1
dy[2] = 2
for i in range(3, n+1):
    dy[i] = dy[i-1] + dy[i-2]
print(dy[n])