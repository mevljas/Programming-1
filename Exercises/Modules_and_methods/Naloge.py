import calendar
import os
import random
import urllib.request


def podvojeni(xs):
    ys = []
    for x in xs:
        if x not in ys:
            ys.append(x)
    return ys



def eboran(s):
    r = ''
    for beseda in s.split():
        if r: r += ' '
        r += beseda[::-1]
    return r



def vrzi(kocka):
    metov, strani = kocka.split('d')
    vsota = 0
    for i in range(int(metov)):
        vsota += random.randint(1, int(strani))
    return vsota


def pricakovana_vrednost(kocka, n=10000):
    vsota = 0
    for _ in range(n):
        vsota += vrzi(kocka)
    return vsota / n


def dan(d, m, l):
    n = calendar.weekday(l, m, d)
    #Returns the day of the week (0 is Monday) for year (1970–…), month (1–12), day (1–31).
    return ['ponedeljek', 'torek', 'sreda', 'četrtek', 'petek',  'sobota', 'nedelja'][n]

def najvecja(pot):
    naj_velikost = 0
    naj_datoteka = None
    for ime in os.listdir(pot):  #Return a list containing the names of the entries in the directory given by path.
        datoteka = os.path.join(pot, ime)   #Join one or more path components intelligently.
        # The return value is the concatenation of path and any members of *paths with exactly one directory separator (os.sep) f
        if not os.path.isfile(datoteka):
            continue
        velikost = os.path.getsize(datoteka)
        if velikost >= naj_velikost:
            naj_velikost = velikost
            naj_ime = ime
    return naj_ime





def an_ban_pet_podgan(xs):
    i = 0
    for j in range(len(xs) - 1):
        i = (i + 10) % len(xs)
        xs.pop(i)
    return xs[0]

import itertools
def bogosort(seznam):
    for p in itertools.permutations(seznam):
        for a, b in zip(p, p[1:]):
            if a > b:
                break
        else:
            return list(p)

def xkcd():
    src = urllib.request.urlopen('https://xkcd.com').read().decode('utf-8')
    for line in src.strip().split('\n'):
        if line.startswith('<title>xkcd: '):
            return line[13:-8]














### ^^^ Naloge rešujte nad tem komentarjem. ^^^ ###

import unittest

class TestNalogeModuli(unittest.TestCase):
    def setUp(self):
        import warnings
        warnings.filterwarnings('ignore', category=ResourceWarning)

    def test_podvojeni(self):
        self.assertEqual(podvojeni([5, 1, 3, 1, 1, 3, 8]), [5, 1, 3, 8])
        self.assertEqual(podvojeni([]), [])
        self.assertEqual(podvojeni([1]), [1])
        self.assertEqual(podvojeni([1, 1, 1]), [1])
        self.assertEqual(podvojeni([1, 2, 3, 3, 2, 1]), [1, 2, 3])
        self.assertEqual(podvojeni([1, 2, 3, 1, 2, 3]), [1, 2, 3])

    def test_eboran(self):
        self.assertEqual(eboran('vse je narobe tudi tale stavek'), 'esv ej eboran idut elat kevats')
        self.assertEqual(eboran('a'), 'a')
        self.assertEqual(eboran('ab'), 'ba')
        self.assertEqual(eboran('a b'), 'a b')
        self.assertEqual(eboran('ab cd'), 'ba dc')

    def test_vrzi(self):
        self.assertEqual(vrzi('5d1'), 5)
        self.assertGreaterEqual(vrzi('3d8'), 3)
        self.assertGreaterEqual(vrzi('2d4'), 2)
        self.assertLessEqual(vrzi('2d3'), 6)
        self.assertLessEqual(vrzi('1d8'), 8)
        self.assertEqual(vrzi('20d1'), 20)
        self.assertGreaterEqual(vrzi('2d20'), 2)
        self.assertLessEqual(vrzi('2d20'), 40)

    def test_pricakovana_vrednost(self):
        self.assertEqual(pricakovana_vrednost('5d1', 100), 5)
        self.assertGreaterEqual(pricakovana_vrednost('2d4', 10), 2)
        self.assertLessEqual(pricakovana_vrednost('2d3', 10), 6)
        self.assertAlmostEqual(pricakovana_vrednost('2d3', 2000), 4.0, delta=1.0)
        self.assertAlmostEqual(pricakovana_vrednost('3d8', 2000), 13.5, delta=1.0)
        self.assertAlmostEqual(pricakovana_vrednost('8d3', 2000), 16.0, delta=1.0)

    def test_dan(self):
        self.assertEqual(dan(12, 8, 1924), 'torek')
        self.assertEqual(dan(6, 6, 6), 'torek')
        self.assertEqual(dan(31, 12, 9999), 'petek')
        self.assertEqual(dan(29, 2, 2020), 'sobota')

    def test_an_ban_pet_podgan(self):
        self.assertEqual(an_ban_pet_podgan(["Maja"]), "Maja")
        self.assertEqual(an_ban_pet_podgan(["Maja", "Janja", "Sabina"]), "Maja")
        self.assertEqual(an_ban_pet_podgan(["Maja", "Janja", "Sabina", "Ina"]), "Ina")
        self.assertEqual(an_ban_pet_podgan(["Maja", "Janja", "Sabina", "Ina", "Jasna"]), "Jasna")
        self.assertEqual(an_ban_pet_podgan(["Maja", "Janja", "Sabina", "Ina", "Jasna", "Mojca"]), "Ina")
        self.assertEqual(an_ban_pet_podgan(["Maja", "Janja", "Sabina", "Ina", "Jasna", "Mojca", "Tina"]), "Maja")

    def test_bogosort(self):
        self.assertEqual(bogosort([]), [])
        self.assertEqual(bogosort([1]), [1])
        self.assertEqual(bogosort([4,3,2,1]), [1,2,3,4])
        self.assertEqual(bogosort([5,8,2,1,5]), [1,2,5,5,8])
        self.assertEqual(bogosort([4,4,4,4]), [4,4,4,4])
        self.assertEqual(bogosort([1,0,-1,-2,2]), [-2,-1,0,1,2])

    def test_xkcd(self):
        result = xkcd()
        self.assertRegex(result, '[\w\s]+')
        self.assertLess(len(result), 255)

if __name__ == '__main__':
    unittest.main(verbosity=2)
