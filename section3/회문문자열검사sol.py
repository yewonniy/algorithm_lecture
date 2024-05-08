def palindrome(word):
    word = word.upper()
    if word == word[::-1]: # 핵심! word[::-1] 하면 word가 reverse 된다! but 내 코드처럼 하는 게 나을걸
        return "YES"
    else:
        return "NO"


n = int(input())
for i in range(n):
    word = input()
    print("#%d" %(i+1), palindrome(word))