import math

r = 6.5
c = math.sqrt(2) * r
a, b = map(int, input().split("x"))
if a and b <= c:
    print("да")
else:
    print("нет")