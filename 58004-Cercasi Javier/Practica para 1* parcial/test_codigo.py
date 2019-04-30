import unittest
from codigo import codigo



class TestVigenere(unittest.TestCase):
    def test_primera_palabra(self):

        resultado = codigo('LOUP','PARISVAUTBIENUNEMESSE')
        self.assertEqual(resultado, 'AOLXDJUJEPCTYIHTXSMHP')


    def test_segunda(self):
        resultado= codigo('LIME','HOLAMUNDO')
        self.assertEqual(resultado,'SWXEXCZHZ')

    def test_tercera(self):
        resultado= codigo('UM','TENGAPIEDAD')
        self.assertEqual(resultado,'NQHSUBCQXMX')

    def test_palabra_con_signos(self):
        try:
            codigo('hola','como estas!')
            self.fail()
        except Exception:
            pass        


if __name__ == "__main__":
    unittest.main()