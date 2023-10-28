# Write a program that reads an unspecified number of scores and determines how many scores are
# above or equal to the average and how many scores are below the average. Assume the input numbers
# are separated by one space in one line.

def prompt_numbers():
    numbers_input = input("Enter numbers between 1 and 100, separated by a space: ")
    return [int(number) for number in numbers_input.split()]


numbers = prompt_numbers()
average = sum(numbers) / len(numbers)
count_below_average = sum(1 for num in numbers if num < average)
count_above_average = sum(1 for num in numbers if num > average)
print(f"Average: {average}")
print(f"Average Count: {numbers.count(average)}")
print(f"Below Average: {count_below_average}")
print(f"Above Average: {count_above_average}")
