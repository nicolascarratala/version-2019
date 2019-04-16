class NotAListException(Exception):
    pass


class NotAllNumberInListException(Exception):
    pass
    
def find_max(list_of_numbers):
        if not list_of_numbers :
                return None
        else :
                max_number = list_of_numbers[0]
                for x in list_of_numbers:
                        if not isinstance(list_of_numbers [x], int):
                                raise Exception('not a number')
                        if max_number < float (x):
                                max_number = float(x)
        return max_number

def find_max(list_of_numbers):
    if not isinstance(list_of_numbers, list):
        raise NotAListException('argument is not a list')

    max_number = None
    if not list_of_numbers:
        return None
    for single_number in list_of_numbers:
        if not isinstance(single_number, int):
            raise NotAllNumberInListException('{} is not a number'.format(single_number))
        if max_number is None or max_number < single_number:
            max_number = single_number

    return max_number