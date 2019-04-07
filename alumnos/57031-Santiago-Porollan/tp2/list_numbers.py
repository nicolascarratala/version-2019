def find_max(list_of_numbers):
    max=-9
    for item in list_of_numbers:
        if item>max:
            max=item
    if max != -9:
        return max
    else :
        return None