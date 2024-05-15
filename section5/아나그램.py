def anagram():
    word = input()
    dic = dict()
    for x in word:
        dic[x] = 0
    for x in word:
        dic[x] += 1
    return dic


dic1 = anagram()
dic2 = anagram()

for key, value in dic1.items():
    if not(key in dic2) or dic2[key] != value:
        print("NO")
        break
else:
    print("YES")