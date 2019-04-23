import unittest
from interfaz_codif import interfaz 

class test_codif(unittest.TestCase):

    def test_interfaz_1 (self):
        code = interfaz('philipp', 'con')
        self.assertEqual('rvvnwcr', code)

    def test_interfaz_2 (self):
        code = interfaz('wikihowisthebest', 'lime')
        self.assertEqual('hqwmswimdbtimmex', code)

    def test_interfaz_3 (self):
        code = interfaz(1, 16)
        self.assertEqual('El programa admite unicamente letras del abecedario', code)        

    def test_codif_4 (self):
        code = interfaz('_', '!')
        self.assertEqual('El programa admite unicamente letras del abecedario', code)        
        

    def test_codif_5 (self):
        code = interfaz('', '')
        self.assertEqual('ingrese una palabra para crear el codigo y una palabra a codificar', code)   

    def test_codif_6 (self):
        code = interfaz('philipp', '')
        self.assertEqual('ingrese una palabra para crear el codigo', code)  

    def test_codif_7 (self):
        code = interfaz('', 'philipp')
        self.assertEqual('ingrese una palabra a codificar', code)  

    def test_codif_8 (self):
        code = interfaz('lime', 'philipp')
        self.assertEqual('la palabra usada para crear el codigo debe ser mas corta que la palabra a codificar', code)  

    def test_interfaz_9 (self):
        code = interfaz('philipp', 16)
        self.assertEqual('El programa admite unicamente letras del abecedario', code)

    def test_interfaz_10 (self):
        code = interfaz(123456789, 'philipp')
        self.assertEqual('El programa admite unicamente letras del abecedario', code)

    def test_interfaz_11 (self):
        code = interfaz(16, 'philipp')
        self.assertEqual('El programa admite unicamente letras del abecedario', code)


if __name__ == '__main__':
   unittest.main()