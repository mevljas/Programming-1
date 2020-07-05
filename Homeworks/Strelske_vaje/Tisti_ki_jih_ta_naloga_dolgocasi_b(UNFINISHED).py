'''
Že znati programirati, in to v Pythonu?
Nekje med topom in ciljem je drevo (lahko je tudi zelo visoko;
morda fižol, ki gre v nebo). Na veji tega drevesa (ali fižola) sedi prašič.
Z isto kroglo bi radi zadeli prašiča in cilj.
Napišite torej program,
ki prebere oddaljenost do cilja ter oddaljenost in višino prašiča.
Program naj izpiše kot in hitrost, s katero je potrebno ustreliti kroglo.

Drugo nalogo lahko rešite na dva načina.
Napišete lahko program, ki s takšnim ali
drugačnim poskušanjem odkrije rešitev.
Lahko pa uporabite svoje znanje fizike ali matematike.
Ali, še boljše, povadite oboje.


https://en.wikipedia.org/wiki/Projectile_motion#Angle_.CE.B8_required_to_hit_coordinate_.28x.2Cy.29
https://math.stackexchange.com/questions/273414/finding-the-angle-and-velocity-to-hit-a-target-in-t-seconds
https://www.omnicalculator.com/physics/projectile-motion


'''

from math import *

g = 9.81
x = float(input("Vpisi oddaljenost do cilja."))
y = 0
#x1 = float(input("Vpisi oddaljenost do prasica."))
#y1 = float(input("Vpisi visino prasica."))
t = 5
#v = (sqrt(x**2 + (y + 0.5 * g * t**2)**2)) / t
v = (sqrt(x**2 + (y + 0.5 * g * t**2)**2)) / t
#a = degrees(acos(x / (v * t)))
a = degrees(acos(x / (v * t)))
#a = degrees(atan((v**2 + sqrt(v**4 - g * (g* x1**2 + 2 * y1 * v**2))) / (g * x1)))
#a2 = degrees(atan((v**2 - sqrt(v**4 - g * (g* x1**2 + 2 * y1 * v**2))) / (g * x1)))

print("Kroglo je potrebno ustreliti pod kotom ", a," °")
print("Kroglo je potrebno ustreliti s hitrostjo ",v ," m/s")

#print(a2)












