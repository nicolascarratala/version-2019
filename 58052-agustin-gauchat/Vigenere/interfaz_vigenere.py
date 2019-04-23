import unittest

from codificacion_vigenere import codificacion_to_vigenere
from decodificacion_vigenere import decodificacion_to_vigenere

def interfaz():
    op = int(input('1- Codificar \n2- Decodificar\n>>'))

    if op == 1:
        palabra = str(input('Ingrese texto a codificar: '))
        clave = str(input('Ingrese clave de codificacion: '))
        print('Codificacion: ' + codificacion_to_vigenere(palabra, clave))

    if op == 2:
        palabra = str(input('Ingrese texto a decodificar: '))
        clave = str(input('Ingrese clave de codificacion: '))
        print('Decodificacion: ' + decodificacion_to_vigenere(palabra, clave))
    
    if op != 1 and op != 2:
        interfaz()