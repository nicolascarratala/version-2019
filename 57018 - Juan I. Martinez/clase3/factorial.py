#para hacerlo de forma recursiva
def factorial(n):
    if n == 1:
        return 1
    else: 
        return n * factorial(n-1)

'''
version 1

def factorial(nro):
    fct = 1
    for number in range(1, nro+1):
        fct *= number

    return fct  

'''