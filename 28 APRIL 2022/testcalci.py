import unittest
from calci import BasicCalculator
b = BasicCalculator(10,5)
class TestBasicCalculator(unittest.TestCase):

    def test_do_addition(self):
        result = b.do_addition()
        self.assertEqual(result, 15)

    def test_do_substraction(self):
        result = b.do_substraction()
        self.assertEqual(result, 5)

    def test_do_multiplication(self):
        result = b.do_multiplication()
        self.assertEqual(result,50)

    def test_do_division(self):
        result = b.do_division()
        self.assertEqual(result,2)

if __name__ == '__main__':
    unittest.main()