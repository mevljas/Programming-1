from math import *

a = int(input("Vpiši a: "))
b = int(input("Vpiši b: "))
c = int(input("Vpiši c: "))

d = b**2 - 4 * a * c

if d > 0:
    x1 = (-b + sqrt(d)) / (2 * a)
    x2 = (-b - sqrt(d)) / (2 * a)

    if x1 == x2:
        print("Enacba ima eno realno rešitev: ", x1)
    else:
        print("Enacba ima dve realni rešitvi: ", x1, " in ", x2)
else:
    print("Enačba nima realnih rešitev.")

