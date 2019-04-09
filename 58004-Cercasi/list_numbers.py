def find_max (list_of_numbers):
    if not list_of_numbers:
        return None
    
    inicio=list_of_numbers[0]
    
    cantidad=len(list_of_numbers)
       
    for vuelta in range(cantidad):
    

        if list_of_numbers[vuelta] >inicio:
            inicio=list_of_numbers[vuelta]
        
    return inicio