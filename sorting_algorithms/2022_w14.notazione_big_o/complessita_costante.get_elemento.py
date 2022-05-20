import sys
from utils import timeit

@timeit
def get_elemento(elementi, indice):
    return elementi[indice]

for numero_elementi in [10, 100, 1000, 10000, 100000, 1000000, 10000000]:
    print(f"Elementi: {numero_elementi}")
    elementi = [x for x in range(numero_elementi)]
    get_elemento(elementi, 8)
    print()
