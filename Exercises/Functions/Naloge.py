from math import *


def naj(xs):
    max_st = None
    for i in xs:
        if max_st == None or i > max_st:
            max_st = i

    return max_st


def naj_abs(xs):
    max_st = None
    for i in xs:
        if max_st == None or abs(i) > abs(max_st):
            max_st = i

    return max_st



def ostevilci(xs):
    seznam = []
    i = 0
    for n in xs:
        seznam.append((i, n),)
        i += 1
    #mogoce uporaba enumerate?
    return  seznam


def bmi(osebe):
    dvojka =[]
    for oseba in osebe:
        ime, teza, visina = oseba
        dvojka.append((ime, (teza / ((visina / 100)**2) )))
    return  dvojka


def bmi2(ime, teza, visina):
    dvojka =[]
    osebe = zip(ime, teza, visina)
    for oseba in osebe:
        ime, teza, visina = oseba
        dvojka.append((ime, (teza / pow(visina / 100 ,2))))
    return  dvojka



def prastevila(n):
    st_prastevil = 0
    for i in range(1 , n):
        st_deljiteljev = 0
        for j in range(1, i + 1):
            if i % j == 0:
                st_deljiteljev += 1
        if st_deljiteljev == 2:
            st_prastevil += 1
    return st_prastevil


def palindrom(s):
    for a,b in zip(s, reversed(s)):
        if a != b:
            return False

    return True

def palindromska_stevila():
    naj_produkt = 0
    for i in range(100, 999 + 1):
        for j in range(100, 999 + 1):
            produkt = i * j
            if palindrom(str(produkt)) and produkt > naj_produkt:
                naj_produkt = produkt #zanka v zanki, ni nujno d bo zadnji najvecji
    return naj_produkt


def inverzije(xs):
    st = 0
    for a in xs:
        for b in xs:
            if b == a:
                break
            if b > a:
                st += 1
    return st

### ^^^ Naloge rešujte nad tem komentarjem. ^^^ ###

import unittest


class TestVaje(unittest.TestCase):
    def test_naj(self):
        self.assertEqual(naj([1]), 1)
        self.assertEqual(naj([-1]), -1)
        self.assertEqual(naj([5, 1, -6, -7, 2]), 5)
        self.assertEqual(naj([1, -6, -7, 2, 5]), 5)
        self.assertEqual(naj([-5, -1, -6, -7, -2]), -1)
        self.assertEqual(naj([1, 2, 5, 6, 10, 2, 3, 4, 9, 9]), 10)
        self.assertEqual(naj([-10 ** 10, -10 ** 9]), -10 ** 9)

    def test_naj_abs(self):
        self.assertEqual(naj_abs([1]), 1)
        self.assertEqual(naj_abs([-1]), -1)
        self.assertEqual(naj_abs([10, 12, 9]), 12)
        self.assertEqual(naj_abs([0, 0, 0, 0, 0]), 0)
        self.assertEqual(naj_abs([5, 1, -6, -7, 2]), -7)
        self.assertEqual(naj_abs([1, -6, 5, 2, -7]), -7)
        self.assertEqual(naj_abs([-5, -1, -6, -7, -2]), -7)
        self.assertEqual(naj_abs([100, 1, 5, 3, -90, 3]), 100)
        self.assertEqual(naj_abs([-100, 1, 5, 3, -90, 3]), -100)
        self.assertEqual(naj_abs([-10 ** 10, -10 ** 9]), -10 ** 10)
        self.assertEqual(naj_abs([1, 2, 5, 6, 10, 2, 3, 4, 9, 9]), 10)
        self.assertEqual(naj_abs([1, 2, 5, 6, -10, 2, 3, 4, 9, 9]), -10)

    def test_ostevilci(self):
        self.assertEqual(ostevilci([]), [])
        self.assertEqual(ostevilci([1]), [(0, 1)])
        self.assertEqual(ostevilci([5, 1, 4, 2, 3]), [(0, 5), (1, 1), (2, 4), (3, 2), (4, 3)])

    def test_bmi(self):
        in_out = [
            ([], []),
            ([('Ana', 55, 165), ('Berta', 60, 153)],
             [('Ana', 20.202020202020204), ('Berta', 25.63116749967961)]),
            ([('Ana', 55, 165), ('Berta', 60, 153), ('Cilka', 70, 183)],
             [('Ana', 20.202020202020204), ('Berta', 25.63116749967961), ('Cilka', 20.902385858042937)]),
        ]
        for i, o in in_out:
            for (nu, bu), (n, b) in zip(bmi(i), o):
                self.assertEqual(nu, n)
                self.assertAlmostEqual(bu, b)

    def test_bmi2(self):
        in_out = [
            (([], [], []), []),
            ((['Ana', 'Berta'], [55, 60], [165, 153]),
             [('Ana', 20.202020202020204), ('Berta', 25.63116749967961)]),
            ((['Ana', 'Berta', 'Cilka'], [55, 60, 70], [165, 153, 183]),
             [('Ana', 20.202020202020204), ('Berta', 25.63116749967961), ('Cilka', 20.902385858042937)]),
        ]
        for i, o in in_out:
            for (nu, bu), (n, b) in zip(bmi2(*i), o):
                self.assertEqual(nu, n)
                self.assertAlmostEqual(bu, b)

    def test_prastevila(self):
        self.assertEqual(prastevila(10), 4)
        self.assertEqual(prastevila(11), 4)
        self.assertEqual(prastevila(12), 5)
        self.assertEqual(prastevila(50), 15)
        self.assertEqual(prastevila(100), 25)
        self.assertEqual(prastevila(1000), 168)

    #    def test_prastevila_hard(self):
    #        self.assertEqual(prastevila(10**6), 78498)
    #        self.assertEqual(prastevila(10**7), 664579)

    def test_palindrom(self):
        self.assertEqual(palindrom(''), True)
        self.assertEqual(palindrom('a'), True)
        self.assertEqual(palindrom('aa'), True)
        self.assertEqual(palindrom('ab'), False)
        self.assertEqual(palindrom('aba'), True)
        self.assertEqual(palindrom('abc'), False)
        self.assertEqual(palindrom('abcdefedcba'), True)
        self.assertEqual(palindrom('abcdefgedcba'), False)
        self.assertEqual(palindrom('pericarezeracirep'), True)
        self.assertEqual(palindrom('perica'), False)

    def test_palindromska_stevila(self):
        self.assertEqual(palindromska_stevila(), 906609)

    def test_inverzije(self):
        self.assertEqual(inverzije([]), 0)
        self.assertEqual(inverzije([1]), 0)
        self.assertEqual(inverzije([1, 2]), 0)
        self.assertEqual(inverzije([2, 1]), 1)
        self.assertEqual(inverzije([3, 2, 1]), 3)
        self.assertEqual(inverzije([4, 3, 2, 1]), 6)
        self.assertEqual(inverzije([5, 4, 3, 2, 1]), 10)
        self.assertEqual(inverzije([1, 4, 3, 5, 2]), 4)
        self.assertEqual(inverzije([10, 3, 9, 2, 22, 42, 0, 88, 66]), 12)


if __name__ == '__main__':
    unittest.main(verbosity=2)
