from math import *

kocke = int(input("Vpiši število kock: "))
skatla = 0
while( skatla**2 < kocke):
    skatla += 1

prostor = skatla**2 - kocke
print("Potrebujemo škatlo širine",skatla,"v kateri je prostora še za ",prostor," kock")