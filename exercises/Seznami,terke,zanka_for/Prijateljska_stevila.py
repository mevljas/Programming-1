vsota1 = 0;
vnos = int(input("Vnesi število "))
for i in range(1,vnos):
    if vnos % i == 0:
        vsota1 += i

vsota2 = 0
for i in range(1,vsota1):
    if vsota1 % i == 0:
        vsota2 += i

if vsota2 == vnos:
    print("Število ima prijatelja: ",vsota1)
else:
    print("Število nima prijatelja: ")
