class Node:

    def __init__(self, new_data):
        self.data = new_data
        self.next = None

    def __repr__(self):
        return self.data
