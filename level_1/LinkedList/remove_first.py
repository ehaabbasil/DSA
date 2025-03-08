# Linked List 


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None 
        self.tail = None 
        self.size = 0

    def removeFirst(self, val):

        if self.size == 0:
            print("list is empty")

        if self.size == 1:
            self.head = self.tail = None

        else:
            self.head = self.head.next 
            self.sizei=1 



