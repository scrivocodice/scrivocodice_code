from utils import timeit


@timeit
def binary_search(elements, target):
    """
    Implements binary search in order to find target in a ordered list of
    elements.
    """
    first = 0
    last = len(elements) - 1
    found = False
    while(first <= last and not found):
        middle = (first + last) // 2
        if elements[middle] == target:
            found = True
        else:
            if target < elements[middle]:
                last = middle - 1
            else:
                first = middle + 1
    return found

for numero_elementi in [10, 100, 1000, 10000, 100000, 1000000, 10000000]:
    print(f"Elementi: {numero_elementi}")
    found = binary_search([x for x in range(numero_elementi)], 10)
    print()
