a = input()
stack = []

for x in a:
    if x.isdecimal():
        stack.append(x)
    else:
        int2 = int(stack.pop())
        int1 = int(stack.pop())
        if x == "+":
            stack.append(int1 + int2)
        elif x == "-":
            stack.append(int1 - int2)
        elif x == "*":
            stack.append(int1 * int2)
        else:
            stack.append(int1 // int2)

print(stack[0])