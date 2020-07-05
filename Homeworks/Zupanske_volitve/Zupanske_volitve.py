import collections


def glasov(obkrozeno):
    stevilo_obkrozenih = 0
    for obkrozen in obkrozeno:
        if obkrozen:
            stevilo_obkrozenih += 1
    return stevilo_obkrozenih

def voljeni(obkrozeno, imena):
    obkrozeni = zip(obkrozeno, imena)
    kandidat = None
    for obkrozen, ime in obkrozeni:
        if obkrozen:
            if kandidat == None:
                kandidat = ime
            else:
                return  None
    return kandidat

def najvecji(d):
    naj_vrednost = None
    naj_kljuc = None
    for kljuc, vrednost in d.items():
        if naj_vrednost == None or vrednost > naj_vrednost:
            naj_vrednost = vrednost
            naj_kljuc = kljuc
    return naj_kljuc, naj_vrednost

def pristej(s, t):
    for kljuc, element in t.items():
        if s.get(kljuc,None) == None:
            s[kljuc] = 0
        s[kljuc] += element

def zmagovalec(glasovnice):
    stevilo_glasovnic = len(glasovnice)
    glasovi = collections.defaultdict(int)
    for glasovnica in glasovnice:
        obkrozeno, imena = glasovnica
        voljena = voljeni(obkrozeno, imena)
        if voljena == None:
            stevilo_glasovnic -= 1
        else:
            glasovi[voljena] +=1
    izvoljena = najvecji(glasovi)
    return izvoljena[0], izvoljena[1] / stevilo_glasovnic

def voljeni_vec(obkrozeno, imena):
    stevilo_glasov = collections.Counter(obkrozeno)[True]
    obkrozeni = zip(obkrozeno, imena)
    voljeni = {}
    for obkrozen, ime in obkrozeni:
        if obkrozen:
             voljeni[ime] = 1 / stevilo_glasov
    return voljeni

def ujemanje(obljube, zelje):
    ujem = 0
    stevilo_elementov = len(list(set(obljube).union(zelje)))
    for zelja in zelje:
        if zelja in obljube:
            ujem += 1
    if stevilo_elementov > 0:
        return ujem / stevilo_elementov
    else:
        return 0

def naj_kandidata(kandidati, zelje):
    ujemanje_zelj = {}
    for kandidat, obljube in kandidati:
        ujemanje_zelj[kandidat] = ujemanje(obljube, zelje)
    ujemanje_sortirano = collections.Counter(ujemanje_zelj).most_common()
    prvi = ujemanje_sortirano[0]
    drugi = ujemanje_sortirano[1]
    return prvi[0], drugi[0]






import unittest

class TestObvezna(unittest.TestCase):
    def test_glasov(self):
        self.assertEqual(2, glasov([True, False, False, True]))
        self.assertEqual(1, glasov([True] + [False] * 1000))
        self.assertEqual(20, glasov([True] * 20 + [False] * 1000))
        self.assertEqual(0, glasov([False] * 1000))
        self.assertEqual(0, glasov([]))

    def test_voljeni(self):
        self.assertEqual("Anna", voljeni([True, False, False], ["Anna", "Berta", "Cilka"]))
        self.assertEqual("Berta", voljeni([False, True, False], ["Anna", "Berta", "Cilka"]))
        self.assertEqual("Cilka", voljeni([False, False, True], ["Anna", "Berta", "Cilka"]))
        self.assertEqual("Cilka", voljeni([True], ["Cilka"]))

        self.assertIsNone(voljeni([True, False, True], ["Anna", "Berta", "Cilka"]))
        self.assertIsNone(voljeni([False, False, False], ["Anna", "Berta", "Cilka"]))
        self.assertIsNone(voljeni([False], ["Cilka"]))
        self.assertIsNone(voljeni([True, True, True], ["Anna", "Berta", "Cilka"]))
        self.assertIsNone(voljeni([], []))

    def test_najvecji(self):
        a, b, c, d = "abcd"
        self.assertEqual((d, 42), najvecji({a: 15, b: 30, c: 8, d: 42}))
        self.assertEqual((c, -5), najvecji({a: -10, b: -30, c: -5, d: -42}))
        self.assertEqual((c, "Dani"), najvecji({a: "Anna", b: "Berta", c: "Dani", d: "Cilka"}))
        self.assertEqual((None, None), najvecji({}))

    def test_pristej(self):
        a, b, c, d = "abcd"
        s = {a: 5, b: 6, d: 4}
        t = {b: 3, c: 8}
        self.assertIsNone(pristej(s, t))
        self.assertDictEqual({a: 5, b: 9, c: 8, d: 4}, s)
        self.assertDictEqual({b: 3, c: 8}, t)

        e = {}
        self.assertIsNone(pristej(s, e))
        self.assertDictEqual({a: 5, b: 9, c: 8, d: 4}, s)
        self.assertDictEqual({}, e)

        self.assertIsNone(pristej(e, t))
        self.assertDictEqual({b: 3, c: 8}, e)

    def test_zmagovalec(self):
        zmago, delez = zmagovalec(
            [([False, True, True], ["Berrta", "Ana", "Cilka"]),  # neveljavna
             ([False, True, True], ["Berrta", "Ana", "Cilka"]),  # neveljavna
             ([False, False, True], ["Ana", "Cilka", "Berrta"]), # Berrta
             ([False, True, False], ["Ana", "Berrta", "Cilka"]), # Berrta
             ([False, True, False], ["Berrta", "Ana", "Cilka"])  # Ana
             ])
        self.assertEqual(zmago, "Berrta")
        self.assertAlmostEqual(2 / 3, delez)

        zmago, delez = zmagovalec(
            [([False, True, True], ["Berrta", "Ana", "Cilka"]),  # neveljavna
             ([False, True, True], ["Berrta", "Ana", "Cilka"]),  # neveljavna
             ([False, True, False], ["Ana", "Cilka", "Berrta"]), # Berrta
             ])
        self.assertEqual(zmago, "Cilka")
        self.assertAlmostEqual(1, delez)


    def test_voljeni_vec(self):
        self.assertEqual(
            {"Ana": .5, "Cilka": .5},
            voljeni_vec([False, True, True], ["Berrta", "Ana", "Cilka"]))
        self.assertEqual(
            {"Cilka": 1},
            voljeni_vec([False, False, True], ["Berrta", "Anna", "Cilka"]))
        self.assertEqual(
            {"Cilka": 0.25, "Berrta": 0.25, "Anna": 0.25, "Dani": 0.25},
            voljeni_vec([True] * 4, ["Berrta", "Anna", "Cilka", "Dani"]))
        self.assertEqual({}, voljeni_vec([False, False], ["Ana", "Berta"]))
        self.assertEqual({}, voljeni_vec([], []))


class TestDodatna(unittest.TestCase):
    def test_ujemanje(self):
        self.assertAlmostEqual(1 / 6, ujemanje(list("abc"), list("cdef")))
        self.assertAlmostEqual(0.5, ujemanje(list("abc"), list("acd")))
        self.assertAlmostEqual(0, ujemanje(list("abc"), list("def")))
        self.assertAlmostEqual(0, ujemanje([], list("acd")))
        self.assertAlmostEqual(0, ujemanje(list("acd"), []))
        self.assertAlmostEqual(0, ujemanje([], []))
        self.assertAlmostEqual(1, ujemanje(list("abc"), list("bca")))
        self.assertAlmostEqual(0.5, ujemanje(list("abcdef"), list("abc")))
        self.assertAlmostEqual(0.5, ujemanje(list("defabc"), list("abc")))
        self.assertAlmostEqual(0.5, ujemanje(list("d"), list("ad")))
        self.assertAlmostEqual(0.5, ujemanje(list("d"), list("ad")))
        self.assertAlmostEqual(1, ujemanje(list("d"), list("d")))

    def test_naj_kandidati(self):
        kandidati = [("Ana", list("abc")),
                     ("Berta", list("bcd")),
                     ("Cilka", list("abcdefg")),
                     ("Dani", list("d")),
                     ("Ema", list("adefgh"))]
        self.assertEqual(("Ana", "Berta"), naj_kandidata(kandidati, list("abc")))
        self.assertEqual(("Dani", "Berta"), naj_kandidata(kandidati, list("d")))


if __name__ == "__main__":
    unittest.main()
