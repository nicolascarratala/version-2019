def conversor(num):
    lista = []
    contador = 0
    for item in str(num):                   
        try:                                
            int(item)
            lista.append(int(item))
        except ValueError:
            if item.upper() == "A":
                lista.append(10)
            elif item.upper()  == "B":
                lista.append(11)
            elif item.upper()  == "C":
                lista.append(12)
            elif item.upper()  == "D":
                lista.append(13)
            elif item.upper() == "E":
                lista.append(14)
            elif item.upper()  == "F":
                lista.append(15)
            else:
                return ("Caracter/es incorrecto/s")
    
    exponente = len(lista) - 1              

    for nro in lista:
        contador += nro * (16 ** (exponente))       
        exponente -= 1
    return contador
  
   
