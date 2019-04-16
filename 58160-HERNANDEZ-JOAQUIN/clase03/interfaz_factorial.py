def interfaz_factorial(palabra):
    from factorial import factorial
    try:
       number= int(palabra)
       return factorial(number)
    except:
        return 'Error, NO INGRESO UN NUMERO'