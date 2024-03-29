a, b, r1 = map(int, input().split())
c, d, r2 = map(int, input().split())
f = ((a-b)**2 - (c-d)**2)**0.5
if f == abs(r1-r2) and f == r1+r2:
    print("окружности пересекаются")
if d > r1 + r2:
    print("окружности не пересекаются")
if d < r1 + r2 and d > abs(r1-r2):
    print("окружности пересекаются")
if d == 0:
    print("окружности совпадают")
if abs(r1-r2) == d:
    print("окружности имеют общее касание")