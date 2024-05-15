n = int(input())
note = [input() for _ in range(n)]
poetry = [input() for _ in range(n - 1)]

note.sort()
poetry.sort()

for i in range(n - 1):
    if note[i] != poetry[i]:
        print(note[i])
        break
else:
    print(note[n - 1])
