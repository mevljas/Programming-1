import math
import risar

n = 20  # Število manjših krogov
R = 200  # Radij velikega kroga
x0, y0 = risar.maxX / 2, risar.maxY / 2  # Središče velikega kroga
krogi = []
for i in range(n):
    phi = 2 * math.pi / n
    x = x0 + R * math.cos(phi * i)
    y = y0 + R * math.sin(phi * i)
    barva = risar.nakljucna_barva()
    r = math.sin(phi / 2) * R
    risar.krog(x, y, r, barva)
    for xx, yy in krogi:
        risar.crta(x, y, xx, yy, barva)
    krogi.append((x, y))
risar.stoj()