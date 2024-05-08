card = []
for i in range(1, 21):
    card.append(i)

for _ in range(10):
    a, b = map(int, input().split())
    for i in range(b-a+2):
        if a-1+i >= b-1-i:
            break
        card[a-1+i], card[b-1-i] = card[b-1-i], card[a-1+i]
        # 인덱스 잘 생각하기! 생각부터 하고 코드 짜라.. 처음에 a-i, b-i로 함 ㅋ 바보

print(card)