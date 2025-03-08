class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def addFirst(self, val):
        new_node = Node(val)

        if self.size == 0:
            self.head = self.tail = new_node


        else:
            new_node.next = self.head 
            self.head = new_node
        self.size+=1 

