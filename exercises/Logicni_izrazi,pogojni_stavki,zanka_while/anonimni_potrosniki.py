vsota = 0
i = 0;

while True:
    vnos = int(input("Cena: "))
    if vnos == 0:
        break;
    vsota += vnos
    i += 1
    if vsota >= 100 or i == 10:
        break;

print("Porabili boste ",vsota," evrov za ",i," stvari")