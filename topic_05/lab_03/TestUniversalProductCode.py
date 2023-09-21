import unittest
from UniversalProductCode import UniversalProductCode


class TestUniversalProductCode(unittest.TestCase):

    def setUp(self):
        self.upc1 = UniversalProductCode("012345678905")
        self.upc2 = UniversalProductCode("012345678906")
        self.upc3 = UniversalProductCode("OneTwoThree")
        self.upc4 = UniversalProductCode("")

    def test_check_digit_valid(self):
        self.assertTrue(self.upc1.is_valid())

    def test_check_digit_invalid(self):
        self.assertFalse(self.upc2.is_valid())

    def test_input_invalid(self):
        self.assertRaises(TypeError, self.upc3.is_valid)

    def test_input_empty(self):
        self.assertRaises(TypeError, self.upc4.is_valid)

if __name__ == '__main__':
    unittest.main()
