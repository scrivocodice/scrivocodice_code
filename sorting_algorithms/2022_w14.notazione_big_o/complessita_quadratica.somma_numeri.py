from utils import timeit, get_matrice

@timeit
def somma_numeri_matrice(matrice):
    somma = 0
    for riga in matrice:
        for numero in riga:
            somma += numero
    return somma

for elementi in [10, 100, 1000, 10000]:
    print(f"Elementi: {elementi}")
    matrice = get_matrice(elementi, elementi)
    somma_numeri_matrice(matrice)
    print()

