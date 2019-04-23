def find_max(list_of_numbers):

    if not isinstance (list_of_numbers, list):
        raise Exception()

    if not list_of_numbers:
        return None
    
    
    max_number = list_of_numbers[0]
    c=0
    v=len(list_of_numbers)

    for num in range(v):
        if max_number < list_of_numbers[num]:
            max_number = list_of_numbers[num]
    if num > c:
        c =num

    

    return max_number