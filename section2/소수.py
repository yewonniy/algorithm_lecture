n = int(input())

cnt = 0
for i in range(2, n+1):
    for j in range(2, int((i ** (1/2) + 1) + 0.5)):
        if i % j == 0:
            print(i, int((i ** (1/2) + 1) + 0.5) -1)
            break
        if j == int((i ** (1/2) + 1) + 0.5) -1:
            print(i, int((i ** (1/2) + 1) + 0.5) -1)
            cnt += 1

print(cnt + 1)