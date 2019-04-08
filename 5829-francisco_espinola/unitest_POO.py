import unittest
from POO2_video27 import coche


class TestCoche(unittest.TestCase):
   def test_inicial(self):
       micoche=coche()
       self.assertEqual(micoche.enmarcha, False)

   def test_arrancar_coche(self):
       micoche=coche()
       micoche.arrancar(True)
       self.assertEqual(micoche.enmarcha, True)

   def test_apagar_coche(self):
       micoche2=coche()
       micoche2.arrancar(False)
       self.assertEqual(micoche2.enmarcha, False)  # te lo dejo a vos

if __name__ == '__main__':
   unittest.main()