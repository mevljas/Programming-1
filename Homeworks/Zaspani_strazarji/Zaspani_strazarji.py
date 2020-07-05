from collections import defaultdict


def razberi(vrstica):
    splitana_vrstica = vrstica.split(" ")
    dolzina_vrstice = len(splitana_vrstica)
    datum = splitana_vrstica[0].replace("[","")
    datum = datum.split("-")
    cas = splitana_vrstica[1].replace("]","")
    cas = cas.split(":")
    if dolzina_vrstice == 6:
        return(int(datum[0]),int(datum[1]),int(datum[2]),int(cas[0]),int(cas[1]),splitana_vrstica[2],int(splitana_vrstica[3].replace("#","")))
    elif dolzina_vrstice == 4:
        return(int(datum[0]),int(datum[1]),int(datum[2]),int(cas[0]),int(cas[1]),splitana_vrstica[2],None)


def preberi_datoteko(ime_datoteke):
    seznam_trojk = []
    f = open(ime_datoteke)
    file = sorted(f)
    current_guard = None
    fall_time = None
    wakeup_time = None
    for vrstica in file:
        razbrana_vrstica = razberi(vrstica)
        leto, mesec, dan, ura, minuta, guard, id = razbrana_vrstica
        if guard == 'Guard':
            current_guard = id
        elif guard == 'falls':
            fall_time = minuta
        elif guard == 'wakes':
            wakeup_time = minuta
            seznam_trojk.append((current_guard, fall_time, wakeup_time))
    f.close()
    return seznam_trojk

def izpis_dogodka(strazar, spi, zbudi):
    return(f"{strazar:4}: {spi:02}-{zbudi:02}")

def naj_drugi(pari):
    max_prvi = pari[0][0]
    max_drugi = pari[0][1]
    for par in pari:
        prvi, drugi = par
        if drugi > max_drugi:
            max_prvi = prvi
            max_drugi = drugi
    return max_prvi

def naj_zaspanec(dogodki):
    spanje = defaultdict(int)
    for strazar, zaspal, zbudil in dogodki:
         spanje[strazar] += zbudil - zaspal
    return  max(spanje, key=spanje.get) #kljuc z najvecjo vrednostjo



def kdaj_spi(strazar, dogodki):
    minute = defaultdict(int)
    for strazar1, zaspal, zbudil in dogodki:
        if strazar == strazar1:
            for i in range(zaspal, zbudil):
                minute[i] += 1
    return  max(minute, key=minute.get) #kljuc z najvecjo vrednostjo



def naj_cas(dogodki):
    dogodki2 = dogodki
    strazarji_minute = defaultdict(int)
    for dogodek in dogodki:
        strazar, spal, zbudil = dogodek
        for dogodek2 in dogodki2:
            strazar2, spal2, zbudil2 = dogodek2
            if strazar == strazar2:
                for i in range(spal2, zbudil2):
                    strazarji_minute[(strazar2, i)] += 1
    max_kombinacija = max(strazarji_minute, key=strazarji_minute.get)
    return max_kombinacija










import unittest
import warnings

class Test01Obvezna(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open("primer.txt", "wt") as primer:
            primer.write("""[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up""")

        with open("primer2.txt", "wt") as primer:
            primer.write("""[1518-11-01 00:26] wakes up
[1518-11-01 00:05] falls asleep
[1518-11-05 00:45] falls asleep
[1518-11-04 00:36] falls asleep
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-01 00:55] wakes up
[1518-11-02 00:40] falls asleep
[1518-11-01 00:00] Guard #10 begins shift
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-01 00:30] falls asleep
[1518-11-05 00:55] wakes up""")

    def test_razberi(self):
        self.assertEqual(
            razberi("[1518-11-09 23:58] Guard #853 begins shift"),
            (1518, 11, 9, 23, 58, "Guard", 853))
        self.assertEqual(
            razberi("[1518-04-02 00:30] falls asleep"),
            (1518, 4, 2, 0, 30, "falls", None))
        self.assertEqual(
            razberi("[1518-08-11 00:47] wakes up"),
            (1518, 8, 11, 0, 47, "wakes", None))
        self.assertEqual(
            razberi("[1518-07-05 23:57] Guard #2917 begins shift"),
            (1518, 7, 5, 23, 57, "Guard", 2917))
        self.assertEqual(
            razberi("[1518-09-06 23:57] Guard #73 begins shift"),
            (1518, 9, 6, 23, 57, "Guard", 73))

    def test_preberi(self):
        warnings.filterwarnings("ignore", category=ResourceWarning)

        self.assertEqual(
            preberi_datoteko("primer.txt"),
            [(10, 5, 25),
             (10, 30, 55),
             (99, 40, 50),
             (10, 24, 29),
             (99, 36, 46),
             (99, 45, 55)])
        self.assertEqual(
            preberi_datoteko("primer2.txt"),
            [(10, 5, 26),
             (10, 30, 55),
             (99, 40, 50),
             (10, 24, 29),
             (99, 36, 46),
             (99, 45, 55)])

    def test_izpis_dogodka(self):
        self.assertEqual(izpis_dogodka(1945, 13, 42), "1945: 13-42")
        self.assertEqual(izpis_dogodka(19, 13, 42), "  19: 13-42")
        self.assertEqual(izpis_dogodka(19, 5, 42), "  19: 05-42")
        self.assertEqual(izpis_dogodka(19, 5, 8), "  19: 05-08")

    def test_naj_drugi(self):
        self.assertEqual(naj_drugi([(5, 3), (8, 9), (13, 5), (10, 7)]), 8)

    def test_naj_zaspanec(self):
        warnings.filterwarnings("ignore", category=ResourceWarning)

        primer = preberi_datoteko("primer.txt")
        self.assertEqual(naj_zaspanec(primer), 10)
        primer2 = preberi_datoteko("input.txt")
        self.assertEqual(naj_zaspanec(primer2), 2663)


class Test02Dodatna(unittest.TestCase):
    def test_kdaj_spi(self):
        warnings.filterwarnings("ignore", category=ResourceWarning)

        primer = preberi_datoteko("input.txt")
        self.assertEqual(kdaj_spi(2663, primer), 38)

    def test_naj_cas(self):
        warnings.filterwarnings("ignore", category=ResourceWarning)

        primer = preberi_datoteko("input.txt")
        self.assertEqual(naj_cas(primer), (2917, 35))


if __name__ == "__main__":
    unittest.main()
