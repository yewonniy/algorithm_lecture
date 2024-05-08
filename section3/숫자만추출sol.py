def find_yaksu(num):
    cnt = 0
    for i in range(1, num+1):
        if num % i == 0:
            cnt += 1
    return cnt


s = input()

result = 0
for x in s:
    if x.isdigit(): # 문자열 내에서 숫자만 뽑는 아이디어! : 문자가 숫자인지 판별하는 함수!! isdecimal()은 자연수만 True
        result = result * 10 + int(x)
print(result)
print(find_yaksu(result))