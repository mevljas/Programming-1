'''
Že znate programirati, vendar ne v Pythonu? Potem veste,
da obstajajo if in while in take reči. Napišite program, ki pove,
kako daleč je potrebno ustreliti.
Uporabnik mora vpisovati različne kote in hitrosti,
 dokler ne zadane cilja na podani razdalji.
 Cilj je zadet, če je razlika med pravo in
 dejansko dolžino strela manjša od toliko in toliko.
'''

from math import *

razdalja = 10
ugibaj = True

while(ugibaj):
    print("Ustreli 10 metrov dalec.")
    hitrost = float(input("Vpisi hitrost izstrelka v metrih na sekundo."))
    kot = radians(float(input("Vpisi kot izstrelka v stopinjah.")))
    strel = ((hitrost ** 2) * (sin(2 * kot))) / 9.81
    print("Dolzina strela je ", strel, " metrov.")
    if(abs(razdalja - strel) < 1):
        ugibaj = False
        print("Zadeli ste cilj.")
    else:
        print("Poskusi ponovno.")







