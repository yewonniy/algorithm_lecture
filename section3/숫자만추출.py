def find_yaksu(num):
    cnt = 0
    for i in range(1, num+1):
        if num % i == 0:
            cnt += 1
    return cnt


s = input()

result = 0
for x in s:
    if x.upper() == x.lower(): # 문자열 내에서 숫자만 뽑는 아이디어! : 숫자는 대문자나 소문자나 똑같다!ㅎㅎㅎㅎㅎ><
        result = result * 10 + int(x)
print(result)
print(find_yaksu(result))