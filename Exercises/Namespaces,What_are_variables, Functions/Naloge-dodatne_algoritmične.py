def count(n):
    while n > 9:
        sum = 0
        for i in str(n):
            sum += int(i)
        n = sum
    return n

def postnina(n):
    cene = []
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            for c in range(1, n + 1):
                if a * b * c == n:
                    cene.append(a + b + c)
    return min(cene)

def nic_ena(xs):
    ones_left = 0
    zeros_right = xs.count(0)
    count = [zeros_right]
    for x in xs:
        if x == 0:
            zeros_right -= 1
        else:
            ones_left += 1
        count.append(ones_left + zeros_right)
    return min(count)

def postnina(n):
    cene = []
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            for c in range(1, n + 1):
                if a * b * c == n:
                    cene.append(a + b + c)
    return min(cene)



def mask(n):
    s = [[]]
    for i in range(n):
        t = []
        for x in s:
            t.append(x + [0])
            t.append(x + [1])
        s = t
    return s

def potencna(xs):
    rezultat = []
    for mask_bits in mask(len(xs)):
        xs_masked = []
        for mask_bit, x in zip(mask_bits, xs):
            if mask_bit:
                xs_masked.append(x)
        rezultat.append(xs_masked)
    return rezultat

def knjige(xs):
    cilj = sum(xs) / 2
    for ys in potencna(xs):
        if sum(ys) == cilj:
            return True
    return False


### ^^^ Naloge rešujte nad tem komentarjem. ^^^ ###

import unittest

class TestSpremenljivke(unittest.TestCase):
    def test_count(self):
        self.assertEqual(count(12345), 6)
        self.assertEqual(count(999999999), 9)
        self.assertEqual(count(213413512), 4)
        self.assertEqual(count(2147483647), 1)

    def test_postnina(self):
        self.assertEqual(postnina(1), 3)
        self.assertEqual(postnina(6), 6)
        self.assertEqual(postnina(7), 9)
        self.assertEqual(postnina(200), 18)

    def test_nic_ena(self):
        self.assertEqual(nic_ena([0, 0, 1, 0, 1]), 1)
        self.assertEqual(nic_ena([0, 0, 1, 1, 1]), 0)
        self.assertEqual(nic_ena([0, 1, 0, 1, 0]), 2)
        self.assertEqual(nic_ena([1, 1, 1, 1, 0, 0, 0]), 3)
        self.assertEqual(nic_ena([1, 0, 0, 0, 1, 1, 1, 0]), 2)
        self.assertEqual(nic_ena([0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0]), 9)

    def test_mask(self):
        self.assertEqual(set(map(tuple,mask(0))), set(map(tuple,[[]])))
        self.assertEqual(set(map(tuple,mask(1))), set(map(tuple,[[0], [1]])))
        self.assertEqual(set(map(tuple,mask(2))), set(map(tuple,[[0, 0], [0, 1], [1, 0], [1, 1]])))
        self.assertEqual(set(map(tuple,mask(3))), set(map(tuple,[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]])))
        self.assertEqual(len(mask(10)), 1024)

    def test_potencna(self):
        self.assertEqual(set(map(tuple,potencna([]))), set(map(tuple,[[]])))
        self.assertEqual(set(map(tuple,potencna([1, 5]))), set(map(tuple,[[], [1], [5], [1, 5]])))
        self.assertEqual(set(map(tuple,potencna([1, 5, 7]))), set(map(tuple,[[], [1], [5], [1, 5], [7], [1, 7], [5, 7], [1, 5, 7]])))
        self.assertEqual(len(potencna([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])), 1024)

    def test_knjige(self):
        self.assertEqual(knjige([10, 20, 30]), True)
        self.assertEqual(knjige([10, 20, 30, 40]), True)
        self.assertEqual(knjige([10, 20, 30, 40, 50]), False)
        self.assertEqual(knjige([23, 51, 51, 153, 25, 51, 59, 39, 35, 91]), False)
        self.assertEqual(knjige([23, 51, 51, 153, 20, 25, 51, 59, 39, 35, 91]), True)


if __name__ == '__main__':
    unittest.main(verbosity=2)
