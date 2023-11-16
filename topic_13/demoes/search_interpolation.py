# Interpolation search example
# Depends on sorted array


def interpolation_search(the_list, target):
    low = 0
    high = len(the_list) - 1

    while low <= high and target >= the_list[low] and target <= the_list[high]:
        pos = low + ((target - the_list[low]) * (high - low)) // (the_list[high] - the_list[low])

        if the_list[pos] == target:
            return pos

        if the_list[pos] < target: # Target is on the right side of the list, so bring up the low value.
            low = pos + 1

        else:
            high = pos - 1
    
    return -1


# Example usage
my_list = [1, 3, 4, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 16, 17, 18, 19]
target = 19
result = interpolation_search(my_list, target)

print(my_list)
if result != -1:
    print(f"Target value {target} found at index {result}.")
else:
    print(f"Target value {target} not found in array.")