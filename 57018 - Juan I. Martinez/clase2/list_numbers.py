#Juan I. Martinez, Legajo 57018
#Version profe
class NotAListException(Exception):
    pass


class NotAllNumberInListException(Exception):
    pass


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


'''
Mi version

def find_max(list_of_numbers):
    if not isinstance(list_of_numbers, list):
        raise Exception('not a number')    
    if not list_of_numbers:
        return None
    else:
        return max(list_of_numbers)


'''
