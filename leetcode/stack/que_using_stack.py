class MyQueue:

    def __init__(self):
        self.items = []
        
    def push(self, x: int) -> None:
        self.items.insert(0,x)
        

    def pop(self) -> int:
        return self.items.pop()
        

    def peek(self) -> int:
        return self.items[-1]
        

    def empty(self) -> bool:
        return not bool(self.items)
