def find_max(list_of_numbers):
        max_number=0
        """
        #otra forma
        if list_of_numbers !=[] :
                for number in list_of_numbers:
                        if number > max_number:
                                max_number=number
        else:
                max_number=None
        """
        if not list_of_numbers:
                max_number = None
        else:
                for number in list_of_numbers:
                        if number > max_number:
                                max_number=number          
        return max_number