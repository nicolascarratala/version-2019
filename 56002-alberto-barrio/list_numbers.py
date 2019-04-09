def find_max(list_of_numbers):
        max_number=0
        if list_of_numbers !=[] :
                for number in list_of_numbers:
                        if number > max_number :
                                max_number=number
        else:
                max_number=None        
        return max_number