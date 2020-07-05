# ljubljana = [28, 30, 25, 28, 30, 32, 35, 28, 25, 27]
# maribor = [30, 28, 26, 34, 26, 32, 34, 30, 28, 28]
ljubljana = [30, 28, 26, 34, 26, 32, 34, 30, 28, 28]
maribor = [28, 30, 25, 28, 30, 32, 35, 28, 25, 27]
par = zip(ljubljana,maribor)
razlika = 0
najtoplejse_mesto = ""


for temperatura in par:
    lj, mb = temperatura
    if abs(lj - mb) > razlika:
        razlika = abs(lj - mb)
        if lj > mb:
            najtoplejse_mesto = "Ljubljana"
        else:
            najtoplejse_mesto = "Maribor"

print(razlika,najtoplejse_mesto)

