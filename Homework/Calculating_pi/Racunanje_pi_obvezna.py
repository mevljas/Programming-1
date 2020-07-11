from random import *
from math import *

r = 1
i = 1
n = 0
st_koordinatov = 1000

while i <= st_koordinatov:
    x = 2 * random() - 1
    y = 2 * random() - 1

    if sqrt(x**2 + y**2) < r:
        n += 1

    i += 1

pi_rac = 4 * n / st_koordinatov
print("PI:", pi_rac)
