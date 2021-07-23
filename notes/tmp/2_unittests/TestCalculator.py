import unittest
from Calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(4, 7), 11)

    def test_divide(self):
        self.assertEqual(self.calculator.div(10, 2), 5)


# python tmp/2_unittests/TestCalculator.py
if __name__ == "__main__":
    unittest.main()
