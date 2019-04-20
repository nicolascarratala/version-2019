import unittest
from factorial import factorial

class NotNumberException(Exception):
    pass

def menu(number1):
    b = int(number1)
    return print('El factorial es:', factorial(b))

def num_entero():
    try:
        num = int(input("Ingrese un numero entero: "))
    except:
        num = num_entero()
        
    return num

num = num_entero()
menu(num)