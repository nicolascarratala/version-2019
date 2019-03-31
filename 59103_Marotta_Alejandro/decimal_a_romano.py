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
    if len(letras) == 3:
        centena = letras [0] 
        decena = letras [1]
        unidad = letras[2]
    if len(letras) == 4:
        mil = letras [0]
        centena = letras [1] 
        decena = letras [2]
        unidad = letras[3]
    
    

    
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


    if centena == '1':
        rc = 'C'
    if centena == '2':
        rc = 'CC'
    if centena == '3':
        rc = 'CCC'
    if centena == '4':
        rc = 'CD'
    if centena == '5':
        rc = 'D'
    if centena == '6':
        rc = 'DC'
    if centena == '7':
        rc = 'DCC'
    if centena == '8':
        rc = 'DCCC'
    if centena == '9':
        rc = 'CM'


    if mil == '1':
        rm = 'M'
    if mil == '2':
        rm = 'MM'
    if mil == '3':
        rm = 'MMM'
    
    #Para el 4000 cambia la notación, voy a hacerlo hasta el 3999
        
    return rm + rc + rd + ru
    


