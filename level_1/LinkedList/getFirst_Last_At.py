# get first, get last, getAt at index 


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def getFirst(self):
        if size == 0:
            print("list is empty")
            return -1
        else:
            return self.head.data

    def getLast(self):
        if size == 0:
            print("list is empty")]
            return -1 
        else:
            return self.tail.data

    def getAt(self, index):
        if size == 0:
            return -1 

        elif index < 0 or index >= self.size:
            print("invalid index")
            return -1 

        else:
            temp = self.head

            for _ in range(index):
                temp = temp.next
            return temp.data 




