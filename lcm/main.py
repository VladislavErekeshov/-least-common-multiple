a, b = map(int, input().split())
for i in range (1, 46340):
    if i % a == 0 and i % b == 0:
        print(i)
        break