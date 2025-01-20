import unittest
from src.calculator import sum, substract, multiply, divide

class CalculatorTest(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(4, sum(2, 2))

    def test_substract(self):
        self.assertEqual(5, substract(10, 5))

    def test_divide(self):
        self.assertEqual(2, divide(10, 5))

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

    def test_multiply(self):
        assert multiply(3,2) == 6

if __name__ == '__main__':
    unittest.main()