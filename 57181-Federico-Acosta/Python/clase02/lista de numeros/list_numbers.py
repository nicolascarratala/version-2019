def find_max(list_of_numbers):
    if not isinstance(list_of_numbers, list):
        raise Exception('not a list')
    
    if not list_of_numbers:
        return None
    else:        
        if not isinstance(list_of_numbers, list):
            raise Exception('not a number')
        else:
            for num in list_of_numbers:
                if isinstance(num, str):
                    raise Exception('contiene letra')
            
            return max(list_of_numbers)
        
        
        