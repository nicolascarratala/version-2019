def find_max(list_of_numbers):
    if list_of_numbers:
        max=list_of_numbers[0]
    else:
        return None
    for number in list_of_numbers:
        if number>max:
            max=number

    return max
