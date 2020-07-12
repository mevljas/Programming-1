import math
import random
import risar

krogi = []
while len(krogi) < 1000:
    x, y = risar.nakljucne_koordinate()
    r = random.randint(20, 80)
    for xx, yy, rr in krogi:
        dist = math.sqrt((xx - x)**2 + (yy - y)**2)
        r = min(r, dist - rr)
        if dist <= rr:
            break
    else:
        krogi.append((x, y, r))
        risar.krog(x, y, r)
risar.stoj()