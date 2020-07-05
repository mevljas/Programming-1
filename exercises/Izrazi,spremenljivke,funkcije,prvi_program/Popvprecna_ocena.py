ana = float(input("Ocena [Ana]?"))
benjamin = float(input("Ocena [Benjamin]?"))
cilka = float(input("Ocena [Cilka]?"))
povprecje = (ana + benjamin + cilka) / 3
min_st = min(ana, benjamin, cilka)
max_st = max(ana, benjamin, cilka)
vsota = ana + benjamin + cilka
srednja_vrednost = vsota - min_st - max_st
print("Povprecje: ",povprecje)
print("Srednja vrednost: ",srednja_vrednost)
