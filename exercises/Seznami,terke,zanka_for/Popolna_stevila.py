vsota = 0;
vnos = int(input("Vnesi število "))
for i in range(1,vnos):  #exclusive
    if vnos % i == 0:
        vsota += i

if(vsota == vnos):
    print("Stevilo je popolno.")
else:
    print("Stevilo ni popolno.")
