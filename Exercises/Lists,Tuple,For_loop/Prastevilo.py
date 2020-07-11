vnos = int(input("Vnesi število "))
delitelji = 0;
for i in range(1,vnos+1):   #exclusive!!!!!
    if vnos % i == 0:
        delitelji += 1
if delitelji == 2:
    print("Število je praštevilo")
else:
    print("Število ni praštevilo")