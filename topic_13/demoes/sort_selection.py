# Example Selection sort
# Finds the smallest item and sets as the first unsorted location


def selection_sort(the_list):
    length_of_list = len(the_list)

    for i in range(length_of_list - 1):
        min_index = i

        for j in range(i + 1, length_of_list):
            if the_list[j] < the_list[min_index]:
                min_index = j

        # Swap the found minimum element with the first element of the unsorted array
        the_list[i], the_list[min_index] = the_list[min_index], the_list[i]

    # print(f"After Pass {the_list}")


my_list = [1,10,23,-2]
print(f"Before swap: {my_list}")
selection_sort(my_list)
print(f"After swap: {my_list}")
