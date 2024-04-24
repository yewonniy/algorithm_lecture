# 파이썬의 함수는 여러 개를 리턴할 수 있다!!!!! => 와 개쩐다...
def add(a, b):
    c = a+b
    d = a-b
    return c, d


print((add(5,2)))


def isPrime(x):
    for i in range(2, x):
        