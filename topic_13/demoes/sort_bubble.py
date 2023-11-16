# Example bubble sort

def bubble_sort(the_list):

    for i in range(len(the_list)):

        for j in range(len(the_list) - 1):

            if the_list[j] > the_list[j+1]:
                # Swap
                the_list[j], the_list[j+1] = the_list[j+1], the_list[j]
                # print(the_list)

        # print(f"After Pass: {the_list}")


my_list = [5, 4, 3, 2, 1]
print(my_list)
bubble_sort(my_list)
print(my_list)
