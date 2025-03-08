# Linked List 

# Add At 

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

    def addLast(self, val):
        new_node = Node(val)
        if self.size == 0:
            # Empty list: Set head and tail to the new node
            self.head = self.tail = new_node
        else:
            # Non-empty list: Link new node to the tail's `next` and update tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1  # Always increment size 



    def addAt(index, val):

        if index < 0 or index > self.size:
            print("Invalid index")

        elif index == 0:
            addFirst(val)

        elif size == 0:
            addLast(val)

        else:
            new_node = Node(val)
            temp = self.addAtHead

            for _ in range(index-1):
                temp = temp.next
            new_node.next = temp.next 
            temp.next = node 
            size+=1 
            






