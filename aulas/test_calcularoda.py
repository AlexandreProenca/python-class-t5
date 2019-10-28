import unittest
from calculadora import somar, dividir, subtrair


class MyTest(unittest.TestCase):

    def test_somar(self):
        self.assertEqual(somar(1,1), 2)

    def test_dividir(self):
        self.assertEqual(dividir(2,1), 2)

    def test_subtrair(self):
        self.assertEqual(subtrair(5,2),  3)


if __name__ == '__main__':
    unittest.main()

