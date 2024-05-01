n, k = map(int,(input().split()))

# arr = []
# for i in range(1, n+1):
#     if n % i == 0: # 약수이다!
#         arr.append(i)
#
# print(arr)
# if len(arr) < k:
#     print(-1)
# else:
#     print(arr[k-1])
cnt = 0
for i in range(1, n+1):
    if n % i == 0:
        cnt += 1
    if cnt == k:
        print(i)
        break
else:
    print(-1)