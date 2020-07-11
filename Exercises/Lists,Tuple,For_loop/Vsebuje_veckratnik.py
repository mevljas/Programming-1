xs = [42, 5, 4, -7, 2, 12, -3, -4, 11, 42, 2]
veckratniki = False
for stevilka in xs:
    if stevilka % 42 == 0:
        veckratniki = True
        break

print(veckratniki)

