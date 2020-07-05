'''
# ljubljana = [28, 30, 25, 28, 30, 32, 35, 28, 25, 27]
# maribor = [30, 28, 26, 34, 26, 32, 34, 30, 28, 28]
ljubljana = [30, 28, 26, 34, 26, 32, 34, 30, 28, 28]
maribor = [28, 30, 25, 28, 30, 32, 35, 28, 25, 27]
par = zip(ljubljana,maribor)
razlika = 0
najtoplejse_mesto = ""


for temperatura in par:
    lj, mb = temperatura
    if abs(lj - mb) > razlika:
        razlika = abs(lj - mb)
        if lj > mb:
            najtoplejse_mesto = "Ljubljana"
        else:
            najtoplejse_mesto = "Maribor"

print(razlika,najtoplejse_mesto)
'''

ljubljana = [28, 30, 25, 28, 30, 32, 35, 28, 25, 27]
maribor = [30, 28, 26, 34, 26, 32, 34, 30, 28, 28]
celje = [28, 32, 30, 31, 32, 28, 27, 26, 25, 25]
koper = [32, 35, 35, 31, 32, 34, 35, 30, 28, 28]
kranj = [28, 27, 30, 32, 28, 27, 26, 28, 30, 25]

vse_temperature = zip(ljubljana,maribor,celje,koper,kranj)
st_dni = 0

for temperatura in vse_temperature:
    lj, mb, ce, kp, kr = temperatura
    povprecje = (lj + mb + ce + kp + kr) / 5
    if povprecje > 30:
        st_dni += 1

print(st_dni)
