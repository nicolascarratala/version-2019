class NotAListException(Exception):
    pass

class NotAllNumberInListException(Exception):
    pass

def find_max(list_of_numbers):
        max_number=0
        if not isinstance(list_of_numbers, list):
                raise NotAListException('argument is not a list')
        if not list_of_numbers:
                max_number = None
        
        for number in list_of_numbers:
                if not isinstance(number,int):
                        raise NotAllNumberInListException('{} is not a number'.format(number))
                if number > max_number:
                        max_number=number          
        return max_number