filmi = ['Poletje v skoljki 2', 'Ne cakaj na maj', 'Pod njenim oknom', 'Kekec', 'Poletje v skoljki', 'To so gadi']
ocene = [6.1, 7.3, 7.1, 8.1, 7.2, 7.7]
skupno = zip(filmi,ocene)

for i in skupno:
    st_presledkov = 0
    f, o = i
    for crka in f:
        if(crka == " "):
            st_presledkov += 1

    if st_presledkov == 2:
        print(f,"(",o,")")