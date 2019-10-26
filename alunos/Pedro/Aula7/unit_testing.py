import unittest
from calculadora import somar, multiplicar


class MyTest(unittest.TestCase):

    def test_somar(self):
        self.assertEqual(somar(1, 2), 3)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(2, 3), 6)


if __name__ == '__main__':
    unittest.main()
