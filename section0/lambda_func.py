# 람다 함수!! = 익명의 함수, 익명의 표현식 (sort함수의 인자로 자주 쓴다)
def plus_one(x):
    return x + 1


print(plus_one(2))

# 위에껄 람다 함수로 바꿔보자
plus_two = lambda x: x + 2  # plus_two 는 함수명이 아니라 변수명! x를 넘기면 x+2를 리턴한다는 뜻
print(plus_two(2))

# 람다함수는 표현식 -> 내장 함수의 인자로 쓸 때 유용@@
a = [1, 2, 3]
print(list(map(plus_one, a)))  # map(함수명, 자료형) -> 뒤의 자료에 앞의 함수를 모두 적용시켜라 map(int, a)의 int도 함수 int!!

# 위에껄 람다함수로 만들자
print(list(map(lambda x: x + 1, a)))  # 위의 기능과 똑같음! a에 들어있는 모든 원소가 x에 대입되어 x+1이 되어 나온다!
