# 리스트 문법!!!!
import random

a = list(range(1,11))
print(a)

random.shuffle(a)
print(a)

a.sort()
print(a)

a.sort(reverse=True)
print(a)

# enumerate! 인덱스랑 value랑..
for x in enumerate(a):
    print(x)

for index, value in enumerate(a):
    print(index, value)

if all(60 > x for x in a):
    print("냐냐")

if all(5 > x for x in a):
    print("냐냐")
else:
    print("므엉")
