# 실패.. 못 풀었음..
arr = list(input())
stack = []

# 숫자는 다 출력하고 기호는 일단 스택에 넣어
for i in range(len(arr)):
    if arr[i].isdigit():
        print(arr[i], end='')
    else: # 나보다 같거나 높은 애는 꺼내
        if len(stack) > 0:
            if arr[i] == "*" or arr[i] == "/":
                if stack[-1] == "*" or stack[-1] == "/":
                    print(stack.pop(), end='')
            elif (arr[i] == "+" or arr[i] == "-") and stack[-1] != "(":
                print(stack.pop(), end='')
            stack.append(arr[i])
            if arr[i] == ")":
                stack.pop()
                while True:
                    n = stack.pop()
                    if n == "(":
                        break
                    print(n, end='')
        else:
            stack.append(arr[i])
while stack:
    print(stack.pop(), end='')