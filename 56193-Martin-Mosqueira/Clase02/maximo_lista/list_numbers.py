def find_max(list_of_numbers):
    maximo=list_of_numbers[0]
    for i in range(0,len(list_of_numbers)):
        if list_of_numbers[i] > maximo:
            maximo=list_of_numbers[i]
    return maximo