# 두 번째 역작....
arr = list(input())
stack = [arr[0]]
cnt = 0

for i in range(1, len(arr)):
    stack.append(arr[i])
    if arr[i - 1] == "(" and arr[i] == ")":
        stack.pop()
        stack.pop()
        cnt += len(stack)
    elif len(stack) > 1 and stack[-2] == "(" and stack[-1] == ")":
        stack.pop()
        stack.pop()
        cnt += 1

print(cnt)