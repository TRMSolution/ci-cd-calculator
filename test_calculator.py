import unittest
from calculator import add, subtract, multiply, divide, power

class TestCalculator(unittest.TestCase):
    
    def test_add(self):
        """Тест сложения"""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
    
    def test_subtract(self):
        """Тест вычитания"""
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(10, 10), 0)
    
    def test_multiply(self):
        """Тест умножения"""
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(0, 5), 0)
    
    def test_divide(self):
        """Тест деления"""
        self.assertEqual(divide(6, 2), 3)
        self.assertEqual(divide(5, 2), 2.5)
        self.assertEqual(divide(-4, 2), -2)
    
    def test_divide_by_zero(self):
        """Тест деления на ноль"""
        with self.assertRaises(ValueError):
            divide(5, 0)
    
    def test_power(self):
        """Тест возведения в степень"""
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(0, 5), 0)

if __name__ == '__main__':
    unittest.main()
