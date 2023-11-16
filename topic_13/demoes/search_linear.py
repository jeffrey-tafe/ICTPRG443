# Linear search example

def linear_search(list, item):
    for index in range(len(list)):
        if list[index] == item:
            return index
    return -1


def main():
    list1 = [12, 4, 16, 8, 1, 7]
    print(list1)
    print(linear_search(list1, 8))
    print(linear_search(list1, 16))
    print(linear_search(list1, 17))


if __name__ == '__main__':
    main()
