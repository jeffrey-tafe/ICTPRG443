# Example Insertion sort
# Not appropriate for large unsorted data sets

def insertion_sort(the_list):
    # Loop from the second element of the array until
    # the last element

    for i in range(1, len(the_list)):

        # This is the element we want to position in its
        # correct place
        key_item = the_list[i]

        # print(f"key_item is {key_item}")
        # Initialize the variable that will be used to
        # find the correct position of the element referenced
        # by `key_item`
        j = i - 1

        # Run through the list of items (the left
        # portion of the array) and find the correct position
        # of the element referenced by `key_item`. Do this only
        # if `key_item` is smaller than its adjacent values.
        while j >= 0 and the_list[j] > key_item:
            # Shift the value one position to the left
            # and reposition j to point to the next element
            # (from right to left)
            the_list[j + 1] = the_list[j]
            j -= 1

            # print(the_list)

        # When you finish shifting the elements, you can position
        # `key_item` in its correct location
        the_list[j + 1] = key_item

        # print(f"After Pass {the_list}")

    return the_list


my_list = [23, 1, 10, 5, -2]
print(f"Before swap: {my_list}")
insertion_sort(my_list)
print(f"After swap:    {my_list}")
