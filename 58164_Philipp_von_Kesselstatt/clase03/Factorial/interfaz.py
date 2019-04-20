from factorial import factorial


def interfaz (n):

    try: 
        int(n)    
        return (factorial(int (n)))    
    except:
        return 'ingrese un numero entero positivo'
        

    
