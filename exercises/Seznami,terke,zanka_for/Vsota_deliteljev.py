vsota = 0;
vnos = int(input("Vnesi število "))
for i in range(1,(vnos+1)):
    print(i)
    if vnos % i == 0:
        vsota += i

print("Vsota je ",vsota)
