import random
import risar

def gore(x0, y0, x2, y2, globina):
    if globina == 0:
        risar.crta(x0, y0, x2, y2)
    else:
        odmik = (x2 - x0) // 4
        x1 = (x0 + x2) / 2
        y1 = (y0 + y2) / 2 + random.randint(-odmik, odmik) 
        gore(x0, y0, x1, y1, globina - 1)
        gore(x1, y1, x2, y2, globina - 1)
gore(0, risar.maxY / 2, risar.maxX, risar.maxY / 2, 10)
risar.stoj()