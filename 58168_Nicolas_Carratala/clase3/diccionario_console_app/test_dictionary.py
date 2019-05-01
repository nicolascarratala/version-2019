import unittest
from dictionary import dictionary_creator

class Main (unittest.TestCase):
    def test_dictionary_creator_hola(self):
        a=dictionary_creator("hola") 
        self.assertEqual(a,{0: 'h', 1: 'o', 2: 'l', 3: 'a'})
    def test_dictionary_creator_chau(self):
        a=dictionary_creator("chau") 
        self.assertEqual(a,{0: 'c', 1: 'h', 2: 'a', 3: 'u'})
    def test_dictionary_creator_queso(self):
        a=dictionary_creator("queso") 
        self.assertEqual(a,{0: 'q', 1: 'u', 2: 'e', 3: 's', 4: 'o'})

if __name__ == "__main__":
    unittest.main()