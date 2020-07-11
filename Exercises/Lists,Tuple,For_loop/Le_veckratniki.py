xs = [42, 84, 126, 168]
veckratniki = True
for stevilka in xs:
    if stevilka % 42 != 0:
        veckratniki = False
        break

print(veckratniki)

