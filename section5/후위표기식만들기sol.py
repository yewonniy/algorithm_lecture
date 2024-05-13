a = input()
stack = []
result = ''

for x in a:
    if x.isdecimal():
        result += x
    else:
        if x == "(":
            stack.append(x)
        elif x == "*" or x == "/":
            while stack and (stack[-1] == "*" or stack[-1] == "/"):
                result += stack.pop()
            stack.append(x)
        elif x == "+" or x == "-":
            while stack and stack[-1] != "(":
                result += stack.pop()
            stack.append(x)
        else:  # x == ")"
            while stack and stack[-1] != "(":
                result += stack.pop()
            stack.pop()
while stack:
    result += stack.pop()

print(result)