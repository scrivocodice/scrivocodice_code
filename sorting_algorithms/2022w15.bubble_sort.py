def bubble_sort(elements):
    target_index = len(elements) - 1
    for indexes in range(target_index, 0, -1):
        for index in range(indexes):
            element = elements[index]
            next_element = elements[index + 1]
            if element > next_element:
                elements[index] = next_element
                elements[index + 1] = element
    return elements


ordered_elements = bubble_sort([20, 19, 18, 17, 16, 15])
print(ordered_elements)
