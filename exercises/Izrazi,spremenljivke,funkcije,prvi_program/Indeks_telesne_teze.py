#v navodilu pise cm, ampak se ne izide --> m
visina = float(input("Višina [m]?"))
masa = int(input("Masa [kg]?"))
itm = masa / (visina / 100)**2
print("Indeks telesne mase: ",itm)
