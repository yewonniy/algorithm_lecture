n = int(input())
arr = list(map(int, input().split()))


def reverse(num):
    result = 0
    while num > 0:
        new = num % 10
        result = (result + new) * 10
        num = num // 10
    return result // 10


def is_prime(num):
    for i in range(2, int(num ** (1/2) + 2)):
        if num % i == 0 and num > 2:
            return False
    return True


for num in arr:
    n = reverse(num)
    if is_prime(n) and n > 1:
        print(n, end=' ')