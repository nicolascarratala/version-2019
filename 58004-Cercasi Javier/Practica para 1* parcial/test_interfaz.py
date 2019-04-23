import unittest
from interfaz_codigo import interfaz_codigo



class TestVigenere(unittest.TestCase):
    def test_primera_palabra(self):

        resultado = interfaz_codigo('LOUP','PARISVAUTBIENUNEMESSE')
        self.assertEqual(resultado, 'AOLXDJUJEPCTYIHTXSMHP')


    def test_segunda(self):
        resultado= interfaz_codigo('LIME','HOLAMUNDO')
        self.assertEqual(resultado,'SWXEXCZHZ')

    def test_tercera(self):
        resultado= interfaz_codigo('UM','TENGAPIEDAD')
        self.assertEqual(resultado,'NQHSUBCQXMX')

    def test_palabra_con_signos(self):
        try:
            interfaz_codigo('hola','como estas!')
            self.fail()
        except Exception:
            pass        


if __name__ == "__main__":
    unittest.main()