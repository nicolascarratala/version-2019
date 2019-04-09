def find_max(list_of_numbers):
        max_number=0
        if not isinstance(list_of_numbers, list):
                raise Exception('not a number')
        if not list_of_numbers:
                max_number = None
        else:
                for number in list_of_numbers:
                        if number > max_number:
                                max_number=number          
        return max_number