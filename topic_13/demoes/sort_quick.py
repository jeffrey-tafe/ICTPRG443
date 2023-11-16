# Example Quick sort
# Better for large data sets
# Uses recursion


def quick_sort(arr):

    if len(arr) <= 1:
        return arr
    else:
        # Choose a pivot element
        pivot = arr[-1]
        left, right = [], []

        # Partition the array into two sub-arrays
        for i in range(len(arr) - 1):
            if arr[i] < pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])

        # Recursively apply the Quick Sort algorithm to the sub-arrays
        return quick_sort(left) + [pivot] + quick_sort(right)


my_list = [3, 8, 2, 1, 5, 4, 6, 7]
print(f"Before swap: {my_list}")
my_list = quick_sort(my_list)
print(f"After swap: {my_list}")
