def anagram():
    word = input()
    dic = dict()
    for x in word:
        dic[x] = dic.get(x, 0) + 1
    return dic


dic1 = anagram()
dic2 = anagram()

for key in dic1.keys():
    if key in dic2.keys():
        if dic2[key] != dic1[key]:
            print("NO")
            break
    else:
        print("NO")
        break
else:
    print("YES")