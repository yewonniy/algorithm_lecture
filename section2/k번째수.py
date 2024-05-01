t = int(input())
for i in range(t):
    n, s, e, k = map(int, input().split())
    num = list(map(int, input().split()))
    arr = num[s-1: e]
    arr.sort()
    print("#" + str(i+1), arr[k-1])
