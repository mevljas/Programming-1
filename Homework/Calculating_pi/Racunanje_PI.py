"""
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

"""

from random import *
from math import *

r = 1
i = 1
n = 0
pi_prejsni = 0
pi_nov = 100
st_koordinatov = 1000

while abs(pi_prejsni - pi_nov) > 0.000001:
    x = 2 * random() - 1
    y = 2 * random() - 1

    if sqrt(x**2 + y**2) < r:
        n += 1

    if i % 1000 == 0:
        pi_prejsni = pi_nov
        pi_nov = 4 * n / i

    i += 1

print("Zadnji  PI:", pi_nov)
print("Prejšni PI:", pi_prejsni)
print("Stevilo točk:", n)





