def palindrome(word):
    word = word.upper()
    i = len(word) - 1
    for x in word:
        if i == len(word) // 2 - 1:
            return "YES"
        if x != word[i]:
            return "NO"
        i -= 1


n = int(input())
for i in range(n):
    word = input()
    print("#%d" %(i+1), palindrome(word))