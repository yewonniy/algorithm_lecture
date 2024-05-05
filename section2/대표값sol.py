n = int(input())
scores = list(map(int, input().split()))

avg = int((sum(scores) / n) + 0.5)

min = 101
for index, score in enumerate(scores): # enumerate.. 활용하자 ㅜㅜ
    tmp = abs(score - avg) # abs를 활용하면 더 간단하게 풀 수 있다!
    if tmp < min:
        min = tmp
        result_score = score
        result_index = index+1
    elif tmp == min:
        if score > result_score:
            result_score = score
            result_index = index+1

print(avg, result_index)