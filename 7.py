n = int(input())
w = False
for x in range(0, 100):
    for y in range(0, 100):
        if 5*x + 7*y == n:
            w = True
            break
    if w:
        print("да")
        break
if not w:
    print("нет")

