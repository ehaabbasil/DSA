# Linked List 

# Adding to Last 
# Display 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insertAtBeginning(self, val):
        new_node = Node(val)
        if self.size == 0:
            # List is empty: Update both head and tail
            self.head = self.tail = new_node
        else:
            # Link new node to the current head and update head
            new_node.next = self.head
            self.head = new_node
        self.size += 1  # Increment size


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

    def get_size(self):
        return self.size


    def display(self):
        temp = self.head

        while temp:
            print(temp.data)
            temp = temp.next
        print()


    def removeFirst(self):
        if self.size == 0:
            print("list is empty")

        elif self.size == 1:
            self.head = self.tail = None
            self.size-=1
        else:
            self.head = self.head.next
            self.size-=1 


if __name__ == '__main__':
    # Create a new LinkedList instance
    llist = LinkedList()
    ll = LinkedList()

    # Insert each letter at the beginning using the method we created
    # llist.insertAtBeginning('fox') 
    # llist.insertAtBeginning('brown') 
    # llist.insertAtBeginning('quick')  
    # llist.insertAtBeginning('the')  
    # llist.addLast('ran away')
    # llist.removeFirst()

    ll.addLast(10)
    ll.addLast(20)
    ll.removeFirst()  # Removes 10, size becomes 1
    ll.removeFirst()  # Removes 20, size becomes 0
    ll.removeFirst()  # Prints "List is empty"

    # Now 'the' is the head of the list, followed by 'quick', then 'brown' and 'fox'

    # Print the list
    llist.display()
