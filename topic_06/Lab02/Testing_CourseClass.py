import unittest
from Lecturer import Lecturer
from Course import Course


class TestingCourseClass(unittest.TestCase):

    def setUp(self):
        self.lecturer1 = Lecturer("001", "Danny", "Sarris", "Technology")
        self.lecturer2 = Lecturer("002", "Julie", "Ruiz", "Technology")
        self.course1 = Course("Python", "thursday", "1130-1330", "Virtual", self.lecturer1)
        self.course2 = Course("Java", "WEDNESDAY", "1130-1330", "Virtual", self.lecturer2)
        self.course3 = Course("BadCourse", "Sunday", "1030-1330", "Virtual", self.lecturer1)
        self.course4 = Course("AnotherBadCourse", "Thur", "1030-1330", "Virtual", self.lecturer1)
        self.course5 = Course("Git", "Friday", "0900-1100", "Virtual", self.lecturer1)

    def test_valid_day_of_week_lower(self):
        result = self.course1.get_day_of_week() == "Thursday"
        self.assertTrue(result)

    def test_valid_day_of_week_upper(self):
        result = self.course2.get_day_of_week() == "Wednesday"
        self.assertTrue(result)

    def test_invalid_day_of_week(self):
        result = self.course3.get_day_of_week() == "Day Of Week Not Set"
        self.assertTrue(result)

    def test_abbeviated_day_of_week(self):
        result = self.course3.get_day_of_week() == "Day Of Week Not Set"
        self.assertTrue(result)

    def test_valid_time(self):
        result = self.course1.get_time() == "1130-1330"
        self.assertTrue(result)

    def test_valid_time_different_time(self):
        result = self.course5.get_time() == "0900-1100"
        self.assertTrue(result)

    def test_invalid_time(self):
        result = self.course3.get_time() == "Time Not Set"
        self.assertTrue(result)

    def test_set_bad_time_colon(self):
        self.course4.set_time("11:30-13:30")
        result = self.course4.get_time() == "Time Not Set"
        self.assertTrue(result)

    def test_set_bad_time_spacing(self):
        self.course4.set_time("1130 - 1330")
        result = self.course4.get_time() == "Time Not Set"
        self.assertTrue(result)

    def test_set_bad_time_no_leading_zero(self):
        self.course4.set_time("900-1100")
        result = self.course4.get_time() == "Time Not Set"
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
