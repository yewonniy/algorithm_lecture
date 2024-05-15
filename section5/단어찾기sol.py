# 해쉬를 이용한 풀이 => dictionary 사용!!

n = int(input())
poem = dict()
for i in range(n):
    word = input()
    poem[word] = 0  # key값은 word, value는 0
for i in range(n-1):
    word = input()
    poem[word] = 1

for key, value in poem.items():
    if value == 0:
        print(key)