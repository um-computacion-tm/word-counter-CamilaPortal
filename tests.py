import unittest
from CountWords import count_words

class TestCountLetters(unittest.TestCase):
    def test1(self):
        result=count_words("hola")
        self.assertEqual(result, {"hola":1})
    
    def test2(self):
        result=count_words("hola mundo")
        self.assertEqual(result, {"hola":1, "mundo":1})
    
    def test3(self):
        result=count_words("hola chau Hola")
        self.assertEqual(result, {"hola":2, "chau":1})
    
    def test4(self):
        result=count_words("La casa en la LUNA")
        self.assertEqual(result, {"la":2, "casa":1, "en":1, "luna":1})

    def test5(self):
        result=count_words("Rojo rojo ROJO roJO")
        self.assertEqual(result, {"rojo":4})

if __name__ == '__main__':
    unittest.main()