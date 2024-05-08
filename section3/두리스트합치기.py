n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

new = arr1 + arr2
new.sort()
for num in new:
    print(num, end=' ')