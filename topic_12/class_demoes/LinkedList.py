from Node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def add_first(self, new_data):
        new_node = Node(new_data)  # Creates a new node
        new_node.next = self.head # The new node points to whatever the head is pointing to (first time, head is pointing to None)
        self.head = new_node # Now head points the new node.  Each new node gets inserted at the beginning of the linked list

    def add_last(self, new_data):
        if self.head is None:
            self.head = new_data
            return

        node = self.head
        while node.next is not None:
            node = node.next
        node.next = Node(new_data)

    def add_after(self, target_node_data, new_data):
        if self.head is None:
            raise Exception("list is empty")

        node = self.head
        while node is not None:
            if node.data == target_node_data:
                new_node = Node(new_data)
                new_node.next = node.next
                node.next = new_node
                return
            node = node.next

        raise Exception(f"Node with data {target_node_data} not found")

    def add_before(self, target_node_data, new_data):
        if self.head is None:
            raise Exception("list is empty")
        node = self.head

        if node.data == target_node_data:
            return self.add_first(new_data)

        while node is not None:
            if node.data == target_node_data:
                new_node = Node(new_data)
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node  # Need to keep track of the previous node
            node = node.next
        raise Exception(f"Node with data {target_node_data} not found")

    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception("list is empty")
        node = self.head

        if node.data == target_node_data:
            self.head = node.next
            return

        while node is not None:
            if node.data == target_node_data:
                prev_node.next = node.next
                return
            prev_node = node  # Need to keep track of the previous node
            node = node.next
        raise Exception(f"Node with data {target_node_data} not found")

    def remove_first(self):
        if self.head is None:
            raise Exception("list is empty")

        node = self.head
        self.head = node.next
        return node

    def __repr__(self):
        node = self.head
        nodes_list = []

        while node is not None:
            nodes_list.append(node.data)   # or use nodes_list.append(str(node))
            node = node.next
        nodes_list.append("None")
        return "->".join(nodes_list)

