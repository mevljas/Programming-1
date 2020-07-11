filmi = [
    ('Poletje v skoljki 2', 6.1),
    ('Ne cakaj na maj', 7.3),
    ('Pod njenim oknom', 7.1),
    ('Kekec', 8.1),
    ('Poletje v skoljki', 7.2),
    ('To so gadi', 7.7),
]
najv_film = ""
najv_ocena = 0.0
prvi_film = ""
vsota_ocena = 0.0
st = 0
print("Filmi z oceno vsaj 7.0:")
for film in filmi:
    f, o = film
    if(o > 7.0):
        print(f)
        if prvi_film == "":
            prvi_film = f
    if(o > najv_ocena):
        najv_film = f
    vsota_ocena += o
    st += 1

print()
print("Film z najvecjo oceno:",najv_film)
print()
print("Ime prvega filma z oceno vasj 7.0:",prvi_film)
print("Povprecna ocena:",(vsota_ocena /st))
print()
print("Filmi, pri katerih je bil posnet drugi del:")

for film in filmi:
    f, o = film
    for film2 in filmi:
        f2, o2 = film2
        if f + (" 2") == f2:
            print(f)