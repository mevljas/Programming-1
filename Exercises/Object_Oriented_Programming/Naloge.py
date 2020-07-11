









import unittest

class TestMesto(unittest.TestCase):
    def test_mesto(self):
        m = Mesto(5, 8)
        self.assertEqual(m.prosto(), 40)

        m.postavi(2, 6)
        self.assertEqual(m.prosto(), 39)

        m.postavi(2, 6)
        self.assertEqual(m.prosto(), 39)

        for x in range(4):
            for y in range(2, 5):
                m.postavi(x, y)
        self.assertEqual(m.prosto(), 27)

        m.porusi(1, 1, 2, 4)
        self.assertEqual(m.prosto(), 33)


class TestLadja(unittest.TestCase):
    def test_1_konstruktor(self):
        ladja = Ladja(42)

    def test_2_natovori_teza(self):
        ladja = Ladja(42)
        ladja.natovori(30)
        self.assertEqual(ladja.skupna_teza(), 30)
        ladja.natovori(4)
        self.assertEqual(ladja.skupna_teza(), 34)
        ladja.natovori(7)
        self.assertEqual(ladja.skupna_teza(), 41)

    def test_3_odstranjevanje(self):
        ladja = Ladja(42)
        self.assertEqual(ladja.odstranjenih(), 0)
        ladja.natovori(30)
        self.assertEqual(ladja.odstranjenih(), 0)
        ladja.natovori(10)

        self.assertEqual(ladja.odstranjenih(), 0)
        ladja.natovori(21)
        self.assertEqual(ladja.odstranjenih(), 1)
        self.assertEqual(ladja.skupna_teza(), 31)

        ladja.natovori(41)
        self.assertEqual(ladja.odstranjenih(), 3)
        self.assertEqual(ladja.skupna_teza(), 41)

        ladja.natovori(50)
        self.assertEqual(ladja.odstranjenih(), 5)
        self.assertEqual(ladja.skupna_teza(), 0)


if __name__ == "__main__":
    unittest.main()
