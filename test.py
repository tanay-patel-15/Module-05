from factorial import factorial
import unittest

class TestFactorial(unittest.TestCase):
  def test__factorial_zero(self):
    self.assertEqual(factorial(0), 1)

  def test_factorial_positive(self):
    self.assertEqual(factorial(7), 5040)

  def test_factorial_negative(self):
    with  self.assertRaises(ValueError):
      factorial(-3)

if __name__ == '__main__':
  # Run the tests.
  unittest.main()
