from Food import Food


foods = {
    Food("Bacon", "Fry"),
    Food("Eggs", "Fry"),
    Food("Eggs", "Boil"),
    Food("Eggs", "Poach"),
    Food("Bacon", "Fry"),
    Food("Bacon", "Fry"),
    Food("Bacon", "Fry"),
    Food("Ice Cream", "Freeze"),
    Food("Fruit", "Wash"),
    Food("Fruit", "Wash")
}

for food in foods:
    print(f"Food: {food.get_name()}, Cooking Method: {food.get_cooking_method()}")
