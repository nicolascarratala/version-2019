import unittest
from menu_factorial import menu

class test_menu_factorial(unittest.TestCase):

    def test_interfaz_factorial_5(self):
        result = menu(5)
        self.assertEqual(result, 120)

    def test_interfaz_factorial_7(self):
        result = menu(7)
        self.assertEqual(result, 5040)

    def test_interfaz_factorial_Bjhdis(self):
        from menu_factorial import NotNumberException
        try:
            result = menu("Bjhdis")
            self.fail()
        except NotNumberException:
            pass

    def test_interfaz_factorial_hola(self):
        from menu_factorial import NotNumberException
        try:
            result = menu("Hola")
            self.fail()
        except NotNumberException:
            pass
            


    
if __name__ == '__main__':
    unittest.main()