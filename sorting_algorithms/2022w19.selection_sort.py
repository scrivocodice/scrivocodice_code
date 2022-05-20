def selection_sort(elements):
    for target_slot in range(len(elements)-1, 0, -1):
        print(f"Target Slot: {target_slot}")
        max_index = target_slot
        for current_index in range(0, target_slot):
            print(f"\tCurrent Index:{current_index}")
            if elements[current_index] > elements[max_index]:
                max_index = current_index
        print(f"\tMaxValue:{elements[max_index]}")
        elements[target_slot], elements[max_index] = elements[max_index], elements[target_slot]
    return elements

print(selection_sort([9,8,7,6,5]))