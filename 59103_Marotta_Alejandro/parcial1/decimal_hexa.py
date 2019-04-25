


def decimal_hexadecimal(decimal): #Defino la funcion
    flag = True
    numero = []
    resultado = 1
    while flag == True : #Mientras que la bandera sea verdadera hacer
        if resultado !=0:   
            resultado = int(decimal/16) #corto el valor de la coma al entero
            resto = (decimal%16) #obtengo el resto
            numero.append(resto) #agrego uno a uno los valores de la lista
            decimal= resultado
        else:
            flag = False   #si resultado = 0 darle a bandera el valor booleano falso
    

    h=''
    for number in numero:  #por cada valor dentro del vector numero 
        if number <=9:
            valor = str(number) #paso los valores numericos a caracteres
        if number ==10:
            valor = 'A'
        if number ==11:
            valor = 'B'
        if number ==12:
            valor = 'C'
        if number ==13:
            valor = 'D'
        if number ==14:
            valor = 'E'
        if number ==15:
            valor = 'F'
        h = h + valor
        hexadecimal = h[::-1] #doy vuelta el string

    return hexadecimal #devuelvo el valor de hexadecimal 

        

        

            
    
    



