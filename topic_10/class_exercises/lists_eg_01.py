fruit_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

# Print list
print(fruit_list)
print()

# Print list in for loop
for fruit in fruit_list:
    print(fruit)
print()

# Print list in for loop on one line
for fruit in fruit_list:
    print(fruit, end=" ")
print()

# Print indexes from list
for index in range(len(fruit_list)):
    print(index)
print()

# Print specific item from list
print(fruit_list[0])
print()

# Print last item from list
print(fruit_list[-1])
print()

# Print second last item from list
print(fruit_list[-2])
print()

# Print specific range in list
print(fruit_list[2:5])
print()

# print last 4 items in rnge
print(fruit_list[-4:-1])
print()

# Overwrite list item
fruit_list[0] = "strawberry"
print(fruit_list)
print()

# Search for item in list
print(f"Index of cherry: {fruit_list.index('cherry')}")

# list item starts with
for fruit in fruit_list:
    if fruit.startswith("b"):
        print(fruit)
print()

# list item starts with
for fruit in fruit_list:
    if fruit.endswith("y"):
        print(fruit)
print()

# copy list
copy_fruit_list = fruit_list.copy()
print(copy_fruit_list)
print()

# count instances of item in list
print(f"Oranges in list: {fruit_list.count('orange')}")
print()

# Add item to list
copy_fruit_list.append("pineapple")
print(copy_fruit_list)
print()

# Insert item at index - Note insert has performance impacts for large lists as recreates list
copy_fruit_list.insert(4, "blueberry")
print(copy_fruit_list)
print()

# pop item from list - Note insert has performance impacts for large lists as recreates list
copy_fruit_list.pop(4)
print(copy_fruit_list)
print()

