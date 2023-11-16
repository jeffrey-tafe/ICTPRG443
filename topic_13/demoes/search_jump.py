# Jump search example
# Depends on array being sorted
# Also known as a block search

import math


def jump_search(my_list, target):
    list_size = len(my_list)
    block_size = int(math.sqrt(list_size))
    left = 0
    right = 0

    # Finding the block where the target could be
    while right < list_size and my_list[right] < target: # While the right variable has not "jumped" passed the list size and we haven't "Jumped" passed the target
        left = right # keep saving the left jump value, in case we need to go backwards when we do the linear search
        right += block_size # work out the next index to jump to

    # Performing a linear search within the block
    for index in range(left, ((left + 1) + block_size)):
        if index < list_size:
            if my_list[index] == target:
                return index

    return -1 # Target value not found in array


# Example usage
the_list = [1, 3, 4, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 16, 17, 18, 19]
target = 15
result = jump_search(the_list, target)

print(the_list)
if result != -1:
    print(f"Target value {target} found at index {result}.")
else:
    print(f"Target value {target} not found in array.")
