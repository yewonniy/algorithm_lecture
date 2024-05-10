n, horse = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()
space = []

mini = -1
maxi = -1  # = result
k = arr[0]

for first_element in range(0, n - horse + 1):
    space.append(arr[first_element])
    while True:
        for j in range(arr.index(k)+1, n):
            space.append(arr[j])
            if len(space) == horse:
                mi = 1000000000
                for i in range(horse-1):
                    mi = min(space[i+1] - space[i], mi)
                mini = max(mi, mini)
                # print(space, "and", mi, "최값은", mini)
                k = space.pop()
                maxi = max(mini, maxi)
                # print(maxi)
        if len(space) > 1:
            k = space.pop()
        if k == arr[-1]:
            a = space.pop()
            k = arr[arr.index(a)+1]
            break

print(maxi)