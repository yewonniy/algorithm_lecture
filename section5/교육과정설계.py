must = list(input())
l = len(must)
n = int(input())
arr = [input() for _ in range(n)]

for i in range(n):
    check = [False for _ in range(l)]
    no = False
    for x in arr[i]:
        if x in must:
            index = must.index(x)
            for k in range(index):
                if not check[k]:
                    no = True
                    break
            check[index] = True
    if no or any(tf == False for tf in check):
        print("NO")
    else:
        print("YES")