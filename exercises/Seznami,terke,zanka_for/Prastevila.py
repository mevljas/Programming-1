for j in range(2,101):
    delitelji = 0;
    for i in range(1, j + 1):  # exclusive!!!!!
        if j % i == 0:
            delitelji += 1
    if delitelji == 2:
        print(j)



