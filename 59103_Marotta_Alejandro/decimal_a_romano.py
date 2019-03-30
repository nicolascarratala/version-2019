def decimal_a_romano(decimal):
    ru =''
    rd =''
    rc =''
    rm =''
    unidad = 0
    decena = 0
    centena = 0
    mil = 0

    letras = str(decimal)
    
   
    
    if len(letras)==1:
        unidad = letras[0]
   
    if len(letras)==2:
        decena = letras [0]
        unidad = letras[1]
     
    

    
    if unidad == '1':
        ru = 'I'
    if unidad == '2':
        ru = 'II'
    if unidad == '3':
        ru = 'III'
    if unidad == '4':
        ru = 'IV'
    if unidad == '5':
        ru = 'V'
    if unidad == '6':
        ru = 'VI'
    if unidad == '7':
        ru = 'VII'
    if unidad == '8':
        ru = 'VIII'
    if unidad == '9':
        ru = 'IX'
    


    if decena == '1':
        rd = 'X'
    if decena == '2':
        rd = 'XX'
    if decena == '3':
        rd = 'XXX'
    if decena == '4':
        rd = 'XL'
    if decena == '5':
        rd = 'L'
    if decena == '6':
        rd = 'LX'
    if decena == '7':
        rd = 'LXX'
    if decena == '8':
        rd = 'LXXX'
    if decena == '9':
        rd = 'XC'

        
    return rd + ru
    


