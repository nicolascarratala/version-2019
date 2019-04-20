class NotAListException(Exception):
    pass

class NotAllNumberInListException(Exception):
    pass


def find_max(list_of_numbers):

    if not isinstance(list_of_numbers, list):
        raise NotAListException('argument is not a list')

    if not list_of_numbers:
        return None
    else:
        max_number = list_of_numbers[0]
        for x in list_of_numbers:
            if not isinstance(x, int):
                raise NotAllNumberInListException('{} is not a number'.format(x))
            if max_number < float(x):
                max_number = float(x)
    return max_number
