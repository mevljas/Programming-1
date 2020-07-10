
# Naloge
Nekatere naloge zahtevajo uporabo matematičnih konstant in funkcij, kot so pi, sqrt (kvadratni koren), sin, cos in podobnih. Python jih nima, vendar jih skrivnostno dobi, če na začetek programa dodamo

`
from math import *
`

## Pretvarjanje temperatur
Program, ki ste ga napisali na predavanjih:

''
temp_C = float(input("Temperature [C]? "))
temp_K = temp_C + 273.15
temp_F = temp_C * 9 / 5 + 32
print(temp_C, "C je enako", temp_K, "K ali", temp_F, "F")
''

spremeni tako, da bo pretvarjal iz Fahrenheitovih stopinj v Celzijeve in Kelvinove. Izpis programa naj izgleda tako:

Temperatura [F]? UPORABNIK VTIPKA 42
42.0 F je enako 278.7055555555555 K ali 5.555555555555555 C
Rešitev
Krog
Napiši program, ki izračuna površino in obseg kroga, katerega polmer poda uporabnik. (Konstanto π boste dobili, če napišete pi, pri čemer mora na začetku programa pisati from math import *, kot smo opisali zgoraj.)

Polmer kroga? UPORABNIK VTIPKA 4.2
Obseg kroga: 26.389378290154262
Površina kroga: 55.41769440932395
Rešitev
Pitagorov izrek
Napiši program, ki uporabnika vpraša po dolžinah katet pravokotnega trikotnika in izpiše dolžino hipotenuze. Kot piše na vrhu strani, za koren uporabimo funkcijo sqrt, ki jo dobimo, če na začetek programa napišemo from math import *.

Kateta? UPORABNIK VTIPKA 3
Kateta? UPORABNIK VTIPKA 4
Hipotenuza: 5.0
Rešitev
Vodnjak
Če vržemo v vodnjak kamen in je v vodnjaku voda, se čez nekaj časa zasliši čof. Napiši program, ki mu uporabnik vpiše, koliko časa je minilo od trenutka, ko smo spustili kamen, do trenutka, ko je reklo čof, program pa izpiše globino vodnjaka. Če ne poznaš enačb, si pomagaj z wikipedijo

Čas [s]? UPORABNIK VTIPKA 1
Globina vodnjaka: 4.905 m
Rešitev
Indeks telesne teže
Napiši program, ki uporabnika vpraša, kako velik (v centimetrih) in kako masiven (v kilogramih) je. V odgovor naj izpiše indeks telesne mase (BMI) uporabnika.

Višina [cm]? UPORABNIK VTIPKA 180
Masa [kg]? UPORABNIK VTIPKA 75
Indeks telesne mase: 23.1481481481
Rešitev
Povprečna ocena
Napiši program, ki mu uporabnik vpiše oceno, ki so jo pri matematiki dobili Ana, Benjamin in Cilka. Program naj izračuna in izpiše povprečno oceno.

Izziv za razmišljujoče tipe: recimo, da ne bi radi izpisali povprečne temveč srednjo oceno. Če so Ana, Benjamin in Cilka dobili 3, 2 in 5, bi radi izpisali 3. Izziv: sprogramiraj to reč brez uporabe pogojnih stavkov ali česa podobno "naprednega". Konkretno, uporabljaj le funkcije input, print, min in max. Namig: min in max lahko prejmeta poljubno število argumentov. Pomisli tudi na to, da imaš samo tri osebe; pri štirih ta trik ne bi vžgal.

Ocena [Ana]? UPORABNIK VTIPKA 2
Ocena [Benjamin]? UPORABNIK VTIPKA 4
Ocena [Cilka]? UPORABNIK VTIPKA 5
Povprečje: 3.6666666666666665
Srednja vrednost: 4.0
Še boljši izziv: recimo, da imamo štiri števila, a, b, c in d. Izpisati želimo tretje število po velikosti. Še vedno uporabljamo le max in min. Namig: mogoče se splača klicati min in max s samo po dvema argumentoma, a večkrat. Morda obstaja tudi kakšna rešitev, kjer kličemo z več argumenti. Morda; ne vem. :)

Rešitev
Površina trikotnika
Napiši program, ki uporabnika vpraša po dolžinah stranic poljubnega trikotnika in izpiše njegovo ploščino, ter ploščini včrtanega in očrtanega kroga.

Dolžina stranice a? UPORABNIK VTIPKA 3
Dolžina stranice b? UPORABNIK VTIPKA 4
Dolžina stranice c? UPORABNIK VTIPKA 5
Površina trikotnika: 6.0
Površina včrtanega kroga: 3.141592653589793
Površina očrtanega kroga: 19.634954084936208
Rešitev
Hitri prsti
Če na začetek programa napišemo

from time import *
bomo, med drugim, dobili funkcijo time, ki vrne čas v sekundah od nekega trenutka v davni preteklosti. Napiši program, ki uporabnika vpraša, koliko je 6 krat 7. Uporabnik bo premislil in vpisal odgovor. Program naj se ne ukvarja z odgovorom ter tem, ali je pravilen ali ne, temveč naj izpiše, koliko sekund je človek potreboval za razmišljanje.

Namig: če veš, koliko je bila ura pred klicem funkcije input in koliko je bila ura po klicu, znaš izračunati, koliko časa je minilo vmes.

Koliko je 6 krat 7? UPORABNIK VTIPKA 42
Za razmišljanje ste porabili 2.503019332885742 s.
Rešitev
Misleči stroj
Napiši program, ki uporabnika vpraša za dve števili. Program izpiše njun produkt. Da pa bi naredil vtis, da razmišlja, produkta ne izpiše takoj, temveč pred tem malo počaka. Za čakanje uporabiš funkcijo sleep, ki jo dobiš, če je na začetku programa napisano

from time import *
Napišeš lahko tri različice programa. Po eni vedno čaka tri sekunde. Po drugi čaka naključno dolgo; koliko časa bo čakal, izžrebaš s funkcijo randint (za katero je potrebno na začetek programa napisati from random import *); čaka naj med eno in petimi sekundami. Tretja pa je takšna: večji ko je produkt, težji je račun. Računalnik naj čaka toliko sekund, kolikor znaša produkt, deljeno z 10. Če mu damo množiti 6 in 7, naj pred izpisom počaka 4.2 sekunde.

Prvo število? UPORABNIK VTIPKA 6
Drugo število? UPORABNIK VTIPKA 7
42.0
