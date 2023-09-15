import unittest as ut
from CourseClass import *

class CourseTestClass(ut.TestCase):
  def setUp(self):
    self.course1 = Course("PRG443PYI", "THURSDAY", "0900 - 1100", "Virtual")

  def test_day_of_week_all_lowercase(self):
    self.course1.set_day_of_week("thursday")
    day = self.course1.get_day_of_week()
    self.assertEqual(day, "Thursday")

  def test_day_of_week_all_uppercase(self):
    self.course1.set_day_of_week("THURSDAY")
    day = self.course1.get_day_of_week()
    self.assertEqual(day, "Thursday")

  def test_day_of_week_not_in_day_range(self):
    self.course1.set_day_of_week("Saturday")
    day = self.course1.get_day_of_week()
    self.assertEqual(day, "Day Of Week Not Set")

if __name__ == '__main__':
  ut.main