from math import *


a = int(input("Dolžina stranice a?"))
b = int(input("Dolžina stranice b?"))
c = int(input("Dolžina stranice c?"))
s = (a + b + c) / 2
p = sqrt(s * (s - a) * (s - b) * (s - c))
print("Površina trikotnika: ",p)
r_vcrtan = p / s
pv = pi * r_vcrtan ** 2
print("Površina včrtanega kroga: ",pv)
r_ocrtan = (a * b * c) / (4 * p)
po = pi * r_ocrtan ** 2
print("Površina očrtanega kroga: ",po)
