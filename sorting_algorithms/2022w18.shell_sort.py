def shell_sort(elements):
    interval = len(elements) // 2
    size = len(elements)
    while interval > 0:
        print(f"\n\n{80*'-'}\nIntervallo: {interval}")
        print(elements)
        for i in range(interval, size):
            print(f"I: {i}")
            temp = elements[i]
            print(f"Temp:{temp}")
            j = i
            while j >= interval and elements[j - interval] > temp:
                elements[j] = elements[j - interval]
                j -= interval
            elements[j] = temp
            print(f"\t{elements}")
        interval //= 2
        print(elements)
    return elements
print(shell_sort([56, 52, 25, 69, 14, 3, 15, 1]))
