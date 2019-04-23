from factorial import factorial

def interfaz_factorial(n):
    try:
        result = int(n)
        return factorial(result)
    except ValueError:
        return 'error'
        
