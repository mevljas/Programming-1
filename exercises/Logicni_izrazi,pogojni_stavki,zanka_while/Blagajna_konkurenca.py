vsota = 0
i = 1
st_izdelkov = int(input("število izdelkov: "))

while i <= st_izdelkov:
    cena = int(input("Cena artikla: "))
    vsota += cena
    i += 1

print("Vsota: ",vsota)