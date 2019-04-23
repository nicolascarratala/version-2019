def decodificacion_to_vigenere(palabra, clave):

    # Funcion de descifrado D(Ci) = (Ci - Ki) mod L
    # Ci es el carácter en la posición i del texto cifrado, Ki viene siendo el carácter de la clave correspondiente a Ci, y L el tamaño del alfabeto.

    abc = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ '
    text_descifrar = ''
    i = 0
    palabra = palabra.upper()
    clave = clave.upper()
    
    for letra in palabra:
        a = abc.find(letra)
        b = abc.find(clave[i % len(clave)])
        suma = a - b
        modulo = int(suma) % len(abc)
        text_descifrar += str(abc[modulo]) 
        i += 1

    return text_descifrar
