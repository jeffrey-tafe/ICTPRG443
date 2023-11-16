# Binary search example
# Dependent on the list being sorted

def binary_search(list, item):
    low = 0
    high = len(list) - 1
    mid = 0


    while low <= high:
        mid = (low + high)//2 # Double forward slashes, is integer division, 7 // 2 will give 3
        if list[mid] < item: # Then need to search the right side of the list
            low = mid + 1
        elif list[mid] > item: # Then need to search the left side of the list
            high = mid - 1
        else:
            return mid # Found it!
    return -1


def main():
    list1 = [12, 4, 16, 8, 1, 7]
    list2 = sorted(list1) # becomes [1, 4, 7, 8, 12, 16]
    print(list2)


    print(binary_search(list2, 16))
    print(binary_search(list2, 7))
    print(binary_search(list2, 1))


if __name__ == '__main__':
    main()
