import unittest
from Stock import Stock


class StockTest(unittest.TestCase):

    def setUp(self):
        self.stock1 = Stock("Intel", "INT", 32.45, 30)
        self.stock2 = Stock("Microsoft", "MSFT", 68.10, 72.10)

    def test_get_name(self):
        result = self.stock1.get_name()
        self.assertEqual(result, "Intel")

    def test_get_symbol(self):
        result = self.stock1.get_symbol()
        self.assertEqual(result, "INT")

    def test_get_previous_closing_price(self):
        result = self.stock1.get_previous_closing_price()
        self.assertEqual(result, 32.45)

    def test_get_current_price(self):
        result = self.stock1.get_current_price()
        self.assertEqual(result, 30)

    def test_get_change_percent(self):
        result = self.stock1.get_change_percent()
        self.assertEqual(result, -7.550077041602473)

    def test_set_previous_closing_price(self):
        self.stock1.set_previous_closing_price(45)
        result = self.stock1.get_previous_closing_price()
        self.assertEqual(result, 45)

    def test_set_current_price(self):
        self.stock1.set_current_price(40)
        result = self.stock1.get_current_price()
        self.assertEqual(result, 40)

    def test__str__(self):
        result = self.stock2.__str__()
        expected = "Name: Microsoft"
        expected += "\nSymbol: MSFT"
        expected += "\nPrevious Closing Price: 68.1"
        expected += "\nCurrent Price: 72.1"
        expected += "\nPrice Change Percentage: 5.873715124816447%"
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
