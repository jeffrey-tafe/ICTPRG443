from LinkedList import LinkedList

my_linked_list = LinkedList()

print(my_linked_list)

# # Add a few nodes to the linked list
my_linked_list.add_first("A")
my_linked_list.add_first("B")
my_linked_list.add_first("C")
my_linked_list.add_first("D")
my_linked_list.add_last("Z")


print(my_linked_list)

# Insert data after a data value

try:
    my_linked_list.add_after("D","DA")
    print(my_linked_list)
    my_linked_list.add_after("B","BA")
    print(my_linked_list)
    my_linked_list.add_after("ZA","ZB")
    print(my_linked_list)
    my_linked_list.add_after("AZ","ZB")
    print(my_linked_list)

except Exception as e:
    print(e)



# Insert data before a data value
try:
    my_linked_list.add_before("D","AD")
    print(my_linked_list)
    my_linked_list.add_before("B","CA")
    print(my_linked_list)
    my_linked_list.add_before("BB","CA")
    print(my_linked_list)

except Exception as e:
   print(e)
   
# Removing nodes
try:
    my_linked_list.remove_node("AD")
    print(my_linked_list)
    my_linked_list.remove_node("ZB")
    print(my_linked_list)
    my_linked_list.remove_node("CA")
    print(my_linked_list)
    my_linked_list.remove_node("ZZ")
    print(my_linked_list)

except Exception as e:
    print(e)

# Removing first
try:
    print(f" The first element out is: {my_linked_list.remove_first()}")
    print(my_linked_list)
    print(f" The first element out is: {my_linked_list.remove_first()}")
    print(my_linked_list)
except Exception as e:
    print(e)
