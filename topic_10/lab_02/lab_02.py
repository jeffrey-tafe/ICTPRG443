# Write a program that reads some integers between 1 and 100 and counts the occurrences of each.
import re


def prompt_numbers():
    numbers_input = input("Enter numbers between 1 and 100, separated by a space: ")
    pattern = r'^(?:100|[1-9][0-9]?|0)(?: (?:100|[1-9][0-9]?|0))*$'

    if not re.match(pattern, numbers_input):
        return None

    return numbers_input.split()


def count_numbers(num_list):
    number_counts = {}
    num_list_copy = num_list.copy()

    while num_list_copy:
        # count instances of number and append to list
        num = num_list_copy[0]
        count = num_list_copy.count(num)
        number_counts[num] = count

        # Remove all instances of number to avoid duplicate counts
        num_list_copy = [n for n in num_list_copy if n != num]

    return number_counts


def output_result(counts_list):

    for number, count in counts_list.items():
        print(f"{number} occurs {count} {time_or_times(count)}")


def time_or_times(value):
    if value > 1:
        return "times"
    return "time"


numbers = prompt_numbers()
counts = count_numbers(numbers)
output_result(counts)
