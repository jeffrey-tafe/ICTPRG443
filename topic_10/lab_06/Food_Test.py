import unittest
from Food import Food  # Assuming your Food class is in a 'food.py' module


class TestFood(unittest.TestCase):
    def test_init(self):
        food = Food("Spaghetti", "Boiling")
        self.assertEqual(food.get_name(), "Spaghetti")
        self.assertEqual(food.get_cooking_method(), "Boiling")

    def test_set_name(self):
        food = Food("Pizza", "Baking")
        food.set_name("Hamburger")
        self.assertEqual(food.get_name(), "Hamburger")

    def test_set_cooking_method(self):
        food = Food("Salad", "None")
        food.set_cooking_method("Chopping")
        self.assertEqual(food.get_cooking_method(), "Chopping")

    def test_str(self):
        food = Food("Steak", "Grilling")
        expected_output = "\n[\n\tName: Steak\n\tCooking Method: Grilling\n]"
        self.assertEqual(str(food), expected_output)

    def test_eq(self):
        food1 = Food("Chicken", "Roasting")
        food2 = Food("Chicken", "Roasting")
        food3 = Food("Pasta", "Boiling")
        self.assertEqual(food1, food2)
        self.assertNotEqual(food1, food3)


if __name__ == '__main__':
    unittest.main()
