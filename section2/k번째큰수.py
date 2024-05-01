n, k = map(int, input().split())
card = list(map(int, input().split()))

sum = set()
for i in range(n):
    for j in range(i+1, n):
        for q in range(j+1, n):
            sum.add(card[i] + card[j]+ card[q])

arr = list(sum)
arr.sort(reverse=True)
print(arr[k-1])