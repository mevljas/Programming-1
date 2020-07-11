def preberi_vrstice(ime_datoteke):
    f = open(ime_datoteke, "r", encoding="utf-8")
    lines = []
    for line in f:
        lines.append(line.strip())
    f.close()
    return lines


# def preberi_vrstice(ime_datoteke):
#     return open(ime_datoteke, "r", encoding="utf-8").read().splitlines()

def preberi_csv(fname):
    sez = []
    for vrstica in preberi_vrstice(fname):
        kraj, vreme, temp = vrstica.split(';')
        sez.append((kraj, vreme, float(temp)))
    return sez


def oblikuj(podatki):
    sez = []
    for kraj, vreme, temp in podatki:
        sez.append(f'Kraj: {kraj}, Vreme: {vreme}, Temperatura: {temp}°C')
    return sez


def oblikuj_tabelo(podatki):
    sez = ['Kraj            Vreme           Temperatura (°C)',
           '------------------------------------------------']
    for kraj, vreme, temp in podatki:
        sez.append(f'{kraj:16}{vreme:16}{temp:16}')
    return sez


def oblikuj_tabelo_f(podatki):
    sez = ['Kraj            Vreme           Temperatura (°F)',
           '------------------------------------------------']
    for kraj, vreme, temp in podatki:
        temp_f = temp * 9 / 5 + 32
        sez.append(f'{kraj:16}{vreme:16}{temp_f:16.1f}')
    return sez


def oblikuj_pike(podatki):
    sez = ['Kraj            Vreme           Temperatura (°F)',
           '------------------------------------------------']
    for kraj, vreme, temp in podatki:
        temp_f = temp * 9 / 5 + 32
        sez.append(f'{kraj:.<16}{vreme:.<16}{temp_f:.>16.1f}')
    return sez

def oblikuj_fc(podatki):
    sez = ['Kraj            Vreme        Temperatura °F (°C)',
           '------------------------------------------------']
    for kraj, vreme, temp in podatki:
        temp_f = temp * 9 / 5 + 32
        temp_fc = f'{temp_f:.1f} ({temp:.1f})'
        sez.append(f'{kraj:.<16}{vreme:.<16}{temp_fc:.>16}')
    return sez


def shrani(vrstice, ime_datoteke):
    f = open(ime_datoteke, "w")
    for vrstica in vrstice:
        f.write(vrstica + '\n')
    f.close()

def najdaljse_besede(s):
    xs = s.split()

    # Poišči dolžino najdaljše besede
    naj = 0
    for word in xs:
        if len(word) > naj:
            naj = len(word)

    # Poišči besede dolžine `naj`
    ys = []
    for word in xs:
        if len(word) == naj:
            ys.append(word)

    return ', '.join(ys)

import os

for f in os.listdir():
    if os.path.splitext(f)[1] == '.py':
        print(f)

ds = ['.']
while ds:
    d = ds.pop()
    for f in os.listdir(d):
        f = os.path.join(d, f)
        if os.path.isdir(f):
            ds.append(f)
        elif os.path.splitext(f)[1] == '.py':
            print(f)


import os

def id3v1(dir):
    os.chdir(dir)
    for fn in os.listdir():
        if os.path.splitext(fn)[1] == '.mp3':
            b = open(fn, 'rb').read()[-128:]
            if b[:3] != b'TAG': continue
            b = b[3:]
            for key, size in [('Title', 30), ('Artist', 30), ('Album', 30), ('Year', 4)]:
                print('{:>6}: {}'.format(key, b[:size].strip(b'x00').decode('ascii')))
                b = b[size:]
            print('  File:', fn)
            print()

id3v1('sponzorska_plata')


# datoteke = [open('datoteke/{}.txt'.format(i)).read() for i in range(10)]
# for i in range(10):
#     for j in range(i):
#         for k in range(0, len(datoteke[i]) - 1000):
#             if datoteke[i][k:k + 1000] in datoteke[j]:
#                 print(i, j)






### ^^^ Naloge rešujte nad tem komentarjem. ^^^ ###

import unittest

class Testi(unittest.TestCase):

    def setUp(self):
        f = open("podatki.txt","w",encoding='utf-8')
        f.write("Ljubljana;oblačno;12.1\n")
        f.write("Maribor;sončno;9\n")
        f.write("Koper;sončno;14.7\n")
        f.close()

        self.podatki = [('Ljubljana', 'oblačno', 12.1), ('Maribor', 'sončno', 9.0), ('Koper', 'sončno', 14.7)]

    def test_preberi_vrstice(self):
        self.assertEqual(preberi_vrstice("podatki.txt"), ["Ljubljana;oblačno;12.1", "Maribor;sončno;9", "Koper;sončno;14.7"])

    def test_preberi_csv(self):
        self.assertEqual(preberi_csv("podatki.txt"), [('Ljubljana', 'oblačno', 12.1), ('Maribor', 'sončno', 9.0), ('Koper', 'sončno', 14.7)])

    def test_oblikuj(self):
        self.assertEqual(oblikuj(self.podatki),
                         ['Kraj: Ljubljana, Vreme: oblačno, Temperatura: 12.1°C',
                          'Kraj: Maribor, Vreme: sončno, Temperatura: 9.0°C',
                          'Kraj: Koper, Vreme: sončno, Temperatura: 14.7°C'])

    def test_oblikuj_tabelo(self):
        self.assertEqual(oblikuj_tabelo(self.podatki),
                         ['Kraj            Vreme           Temperatura (°C)',
                          '------------------------------------------------',
                          'Ljubljana       oblačno                     12.1',
                          'Maribor         sončno                       9.0',
                          'Koper           sončno                      14.7'])

    def test_oblikuj_tabelo_f(self):
        self.assertEqual(oblikuj_tabelo_f(self.podatki),
                         ['Kraj            Vreme           Temperatura (°F)',
                          '------------------------------------------------',
                          'Ljubljana       oblačno                     53.8',
                          'Maribor         sončno                      48.2',
                          'Koper           sončno                      58.5'])

    def test_oblikuj_pike(self):
        self.assertEqual(oblikuj_pike(self.podatki),
                         ['Kraj            Vreme           Temperatura (°F)',
                          '------------------------------------------------',
                          'Ljubljana.......oblačno.....................53.8',
                          'Maribor.........sončno......................48.2',
                          'Koper...........sončno......................58.5'])

    def test_oblikuj_fc(self):
        self.assertEqual(oblikuj_fc(self.podatki),
                         ['Kraj            Vreme        Temperatura °F (°C)',
                          '------------------------------------------------',
                          'Ljubljana.......oblačno..............53.8 (12.1)',
                          'Maribor.........sončno................48.2 (9.0)',
                          'Koper...........sončno...............58.5 (14.7)'])

    def test_shrani(self):
        lines = ['prva vrstica', 'druga vrstica', 'tretja vrstica']
        shrani(lines, 'datoteka.txt')
        f = open("datoteka.txt", "r")
        lines_f = f.read().splitlines()
        f.close()
        self.assertEqual(lines_f, lines)

    def test_najdaljse_besede(self):
        self.assertEqual(najdaljse_besede('ob znaku bo ura deset in pet minut'), 'znaku, deset, minut')

if __name__ == '__main__':
    unittest.main(verbosity=2)
