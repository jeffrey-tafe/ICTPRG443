# Write a program that reads in numbers separated by a space in one line and displays distinct numbers
# (i.e., if a number appears multiple times, it is displayed only once). (Hint: Read all the numbers and store
# them in list1. Create a new list list2. Add a number in list1 to list2. If the number is already in the list,
# ignore it.) Here is the sample run of the program:


def prompt_numbers():
    numbers_input = input("Enter numbers between 1 and 100, separated by a space: ")
    return [int(number) for number in numbers_input.split()]


def get_distinct_numbers(number_list):
    distinct_numbers = []
    for number in number_list:
        if number not in distinct_numbers:
            distinct_numbers.append(number)
    return distinct_numbers


def output_result(distinct_numbers):
    print(*distinct_numbers, end=" ")


def main():
    numbers = prompt_numbers()
    distinct_numbers = get_distinct_numbers(numbers)
    output_result(distinct_numbers)


if __name__ == "__main__":
    main()
