import unittest as ut
from Calculator import *

class CalculatorTestCase(ut.TestCase):

  def test_add_both_positive(self):
    answer = add(10, 20)
    self.assertEqual(answer, 30)


  def test_add_both_negative(self):
    answer = add(-10, -10)
    self.assertEqual(answer, -20)

  def test_add_one_positive_one_negative(self):
    answer = add(10, -10)
    self.assertEqual(answer, 0)

  def test_value_error(self):
    with self.assertRaises(ValueError):
      divide("a", "1")

  def test_divide_division_by_zero_error(self):
    with self.assertRaises(ZeroDivisionError):
      divide("10", "0")



  if __name__ == "__main__":
    ut.main()