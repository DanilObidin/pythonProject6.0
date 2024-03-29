z = input()
xy = ["a", "c", "e", "g"]
zv = ["b", "e", "f", "h"]
if z[0] in xy and int(z[1]) % 2 == 0:
    print("белые")
elif z[0] in zv and int(z[1]) % 2 != 0:
    print("белые")
else:
    print("черные")
