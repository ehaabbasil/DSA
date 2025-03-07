# Linked List 

# Adding to Last

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def addLast(self, val):
        temp = Node(val)
        if self.size == 0:
            # Empty list: Set head and tail to the new node
            self.head = self.tail = temp
        else:
            # Non-empty list: Link new node to the tail's `next` and update tail
            self.tail.next = temp
            self.tail = temp
        self.size += 1  # Always increment size 