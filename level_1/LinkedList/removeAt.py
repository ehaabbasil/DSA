 # Linked List 

# Remove at 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def removeFirst(self):

        if self.size == 0:
            print("list is empty")

        if self.size == 1:
            self.head = self.tail = None

        else:
            self.head = self.head.next 
            self.size-=1 

    def removeLast(self):
        if self.size == 0:
            print("list is empty")

        if self.size == 1:
            self.head = self.tail = None

        else:
            temp = self.head 
            for _ in range(self.size-2):
                temp = temp.next 

            self.tail = temp 
            temp.next = None 
            size-= 1 


    def removeAt(self,index):

        if index < 0 or index>=self.size:
            print("invalid arguments")

        elif index == 0:
            removeFirst()

        elif 