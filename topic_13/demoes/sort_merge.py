# Example Merge sort
# Better for large data sets
# Uses recursion


def merge_sort(the_list):

    if len(the_list) > 1:
        # Divide the input list into two halves
        mid = len(the_list) // 2
        left_half = the_list[:mid]
        right_half = the_list[mid:]

        # Recursively sort each half using Merge Sort
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the two sorted halves into a single sorted list
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):

            if left_half[i] < right_half[j]:
                the_list[k] = left_half[i]
                i += 1
            else:
                the_list[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):

            the_list[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            the_list[k] = right_half[j]
            j += 1
            k += 1

    return the_list


my_list = [3,8,2,1,5,4,6,7]
print(f"Before swap: {my_list}")
merge_sort(my_list)
print(f"After swap: {my_list}")
