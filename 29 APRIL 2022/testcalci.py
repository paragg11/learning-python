import unittest
from calci import BasicCalculator
basic_calculator = BasicCalculator(10, 5)
class TestBasicCalculator(unittest.TestCase):

    def test_do_addition(self):
        result = basic_calculator.do_addition()
        self.assertEqual(result, 15)

    def test_do_substraction(self):
        result = basic_calculator.do_substraction()
        self.assertEqual(result, 5)

    def test_do_multiplication(self):
        result = basic_calculator.do_multiplication()
        self.assertEqual(result,50)

    def test_do_division(self):
        result = basic_calculator.do_division()
        self.assertEqual(result,2)

if __name__ == '__main__':
    unittest.main()