# Linked List 

# Remove Last 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def removeLast(self,val):
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
            size -= 1 



            


