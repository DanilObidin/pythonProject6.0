a = [0]
for x in range(1, 200+1):
    if x < 10:
        a.append(x)
    if x < 100 and x >= 10:
        a.append(x // 10)
        a.append(x % 10)
    if x >= 100:
        a.append(x // 100)
        a.append((x // 10) % 10)
        a.append(x % 10)
i = int(input())
print(a[i - 1])

