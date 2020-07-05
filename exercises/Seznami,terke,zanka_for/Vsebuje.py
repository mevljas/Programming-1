xs = [42, 5, 4, -7, 2, 12, -3, -4, 11, 42, 2]
videl_sem_42 = False
for stevilka in xs:
    if stevilka == 42:
        videl_sem_42 = True

print(videl_sem_42)
if videl_sem_42:
    print("Res sem videl 42.")