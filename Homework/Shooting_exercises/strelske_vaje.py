from math import *

hitrost = float(input("Vpisi hitrost izstrelka v metrih na sekundo."))
kot = radians(float(input("Vpisi kot izstrelka v stopinjah.")))
dolzina = ((hitrost**2) * (sin(2 * kot))) / 9.81
print("Dolzina strela je ",  dolzina, " metrov.")
