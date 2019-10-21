terninger = []
def terning_kast(antal_kast = int(input("Hvor mange terningekast? "))):
    for x in range(antal_kast, 0, -1):
        resultat = random.randint(1, 6)
        terninger.append(resultat)
    return resultat

print('before', terninger)
terning_kast() # this is the line which you have missed
print('after', terninger)