import unittest
from Grade import Grade


class GradeTest(unittest.TestCase):

    def setUp(self):
        self.grade = Grade()

    def test_mark_non_numeric(self):
        result = self.grade.set_grade("test")
        self.assertTrue(result == "ERROR")

    def test_mark_out_of_range(self):
        result = self.grade.set_grade(20002)
        self.assertTrue(result == "ERROR")

    def test_mark_negative(self):
        result = self.grade.set_grade(-3)
        self.assertTrue(result == "ERROR")

    def test_mark_hd(self):
        result = self.grade.set_grade(99)
        self.assertTrue(result == "HD")

    def test_mark_d(self):
        result = self.grade.set_grade(77)
        self.assertTrue(result == "D")

    def test_mark_c(self):
        result = self.grade.set_grade(66)
        self.assertTrue(result == "C")

    def test_mark_p(self):
        result = self.grade.set_grade(55)
        self.assertTrue(result == "P")

    def test_mark_f(self):
        result = self.grade.set_grade(0)
        self.assertTrue(result == "F")


if __name__ == '__main__':
    unittest.main()
