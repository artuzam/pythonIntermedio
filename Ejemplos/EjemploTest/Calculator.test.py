import unittest
import Calculator as C


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = C.Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(5, 3), 8)
        self.assertEqual(self.calculator.add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(10, 7), 3)
        self.assertEqual(self.calculator.subtract(-5, -2), -3)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(4, 5), 20)
        self.assertEqual(self.calculator.multiply(-3, 2), -6)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(10, 2), 5)
        self.assertEqual(self.calculator.divide(-8, 4), -2)

        with self.assertRaises(ValueError):
            self.calculator.divide(5, 0)


if __name__ == "__main__":
    unittest.main()
