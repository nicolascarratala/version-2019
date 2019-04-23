def codificacion_to_vigenere(palabra, clave):
    
    # Funcion de cifrado E(Xi)=(Xi +Ki) mod \ L
    # Xi es la letra en la posición i del texto a cifrar, Ki es el carácter de la clave correspondiente a Xi, y L es el tamaño del alfabeto

    abc = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ '
    text_cifrar = ''
    i = 0
    palabra = palabra.upper()
    clave = clave.upper()

    for letra in palabra:
        a = abc.find(letra)
        b = abc.find(clave[i % len(clave)])
        suma = a + b
        modulo = int(suma) % len(abc)
        text_cifrar += str(abc[modulo]) 
        i += 1

    return text_cifrar