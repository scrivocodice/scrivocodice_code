def insertion_sort(elements):
    for target_index in range(1, len(elements)):
        current_index = target_index - 1
        target_element = elements[target_index]
        current_element = elements[current_index]
        while( (current_element > target_element) and (current_index >= 0) ):
            print(f"{elements[current_index]} > {target_element}")
            elements[current_index+1] = current_element
            elements[current_index] = target_element
            current_index -= 1
            current_element = elements[current_index]
        print(elements)
    return elements

insertion_sort([56, 52, 25, 69, 14, 3])
