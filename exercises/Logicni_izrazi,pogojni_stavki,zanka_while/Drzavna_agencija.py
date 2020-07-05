vsota = 0
i = 0
povp = 0.0

while True:
    cena = int(input("Cena artikla: "))
    if cena == 0:
        break
    vsota += cena
    i += 1

if vsota != 0:
    povp = vsota / i

print("Vsota: ",vsota)
print("Povprečna cena: ",povp)