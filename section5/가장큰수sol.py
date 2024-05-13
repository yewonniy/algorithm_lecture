# stack을 이용해서 풀면 됨!!! (나보다 작은 놈이 내 앞에 있으면 걜 없애는 아이디어⭐⭐)

a, n = map(int, input().split())
num = list(map(int, str(a)))
stack = []

for x in num:
    while stack and n > 0 and stack[-1] < x:
        stack.pop()
        n -= 1
    stack.append(x)

if n != 0:  # 더 지워야함
    stack = stack[: -n]  # 뒤쪽 n개의 자료를 날림
print(stack)