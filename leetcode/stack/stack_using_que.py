class MyStack:

    def __init__(self):
        self._items = []
        

    def push(self, x: int) -> None:
        self._items.append(x)
        

    def pop(self) -> int:
        return self._items.pop()
        

    def top(self) -> int:
        return self._items[-1]
        

    def empty(self) -> bool:
        return not bool(self._items)
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

