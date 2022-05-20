from utils import timeit


@timeit
def somma_numeri(numeri):
    somma = 0
    for numero in numeri:
        somma += numero
    return somma

for numero_elementi in [10, 100, 1000, 10000, 100000, 1000000, 10000000]:
    print(f"Elementi: {numero_elementi}")
    elementi = [x for x in range(numero_elementi)]
    somma_numeri(elementi)
    print()
