ljubljana = [28, 30, 25, 28, 30, 32, 35, 28, 25, 27]
maribor = [30, 28, 26, 34, 26, 32, 34, 30, 28, 28]
par = zip(ljubljana,maribor)
celje = [28, 32, 30, 31, 32, 28, 27, 26, 25, 25]
koper = [32, 35, 35, 31, 32, 34, 35, 30, 28, 28]
kranj = [28, 27, 30, 32, 28, 27, 26, 28, 30, 25]

print("Temperatura v Ljubljani:",ljubljana)
for temperatura in par:
    print("Temperatura v Ljubljani in Mariborju:",temperatura)
    lj, mb = temperatura
    print("Razlika temperature med Ljubljano in Mariborjem:",(lj - mb))
    print("Razlika temperature med Ljubljano in Mariborjem (abs):",abs(lj - mb))
    print()

