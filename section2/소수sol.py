n = int(input())

cnt = 0
arr = [0] * (n+1)
for i in range(2, n+1):
    if arr[i] == 0: # 핵심.. (거꾸로 생각!)
        cnt += 1
        for j in range(i, n+1, i): # i 의 배수들을 다 1로 만들기
            arr[j] = 1

print(cnt)