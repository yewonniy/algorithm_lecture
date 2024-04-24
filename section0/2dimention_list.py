# 아래와 같이 2차원 리스트를 만들면 안됨! 같은 걸 참조하니까!!!
a = [[0] * 3] * 3 # x001을 참조하는 포인터 3개 생성
print(a)

a[0][0] = 5
print(a)

# 아래와 같이 만들 것 ㅎㅎ
a = [[0]*3 for _ in range(3)]
print(a)

a[0][0] = 5
print(a)

a[1][2] = 12
print(a)
for x in a:
    print(x)