from codif import cod


def interfaz (word, code):

    if not code and not word:
        return 'ingrese una palabra para crear el codigo y una palabra a codificar'

    if not word:
        return 'ingrese una palabra a codificar'

    if not code:
        return 'ingrese una palabra para crear el codigo'

    if len(code) > len(word):
            try:    
                int(word)
                return 'El programa admite unicamente letras del abecedario'
                    
            except:
                try:
                    int(code)
                    return 'El programa admite unicamente letras del abecedario'
                except:
                    return 'la palabra usada para crear el codigo debe ser mas corta que la palabra a codificar'

    try:    
        int(word)
        return 'El programa admite unicamente letras del abecedario'
            
    except:

        try:
            int(code)
            return 'El programa admite unicamente letras del abecedario'
        except:
            return cod(word, code)
        




word = input('Ingrese la palabra a codificar:    ')

code = input ('Ingrese la palabra con la que se creara el codigo:    ')

print(interfaz(word, code))
    
