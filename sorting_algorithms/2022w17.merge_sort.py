def merge_sort(elements):
    if len(elements) > 1:
        # ---------
        # splitting
        # ---------
        mid = len(elements) // 2
        left = elements[:mid]
        right = elements[mid:]
        merge_sort(left)
        merge_sort(right)

        # ---------
        # merging
        # ---------
        a = b = c = 0
        # ordino elementi sulle due liste
        while a < len(left) and b < len(right):
            if left[a] < right[b]:
                elements[c] = left[a]
                a += 1
            else:
                elements[c] = right[b]
                b += 1
            c += 1
        
        # aggiungo elementi della lista sinistra (se sono di pù)
        while a < len(left):
            elements[c] = left[a]
            a += 1
            c += 1
        
        # aggiungo elementi della lista destra (se sono di pù)
        while b < len(right):
            elements[c] = right[b]
            b += 1
            c += 1

    return elements

print(merge_sort([56, 52, 25, 69, 14, 3]))
