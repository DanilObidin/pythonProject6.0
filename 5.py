a, b = input().split("-")
x = ["a", "b", "c", "d", "e", "f", "g", "h"]
a1 = int(a[1])
b1 = int(b[1])
if abs(b1 - a1) == 1:
    c = x.index(a[0])
    if x[c + 2] == b[0] or x[c - 2] == b[0]:
        print("верно")
    else:
        print("ошибка")
elif abs(b1 - a1) == 2:
    c = x.index(a[0])
    if x[c + 1] == b[0] or x[c - 1] == b[0]:
        print("верно")
    else:
        print("неверно")
else:
    print("неверно")
print(x.index(a[0]))











