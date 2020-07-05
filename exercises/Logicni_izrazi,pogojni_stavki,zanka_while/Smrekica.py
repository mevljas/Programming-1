visina = int(input("Vpiši višino: "))
i = 1
while i <= visina:
    print(" " * (visina - i), end="")
    print("*" * (i * 2 - 1))
    i += 1