class MyStack:
  
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        while len(self.queue1) > 0:
            el1 = self.queue1.popleft()
            self.queue2.append(el1)
        self.queue1.append(x)
        while len(self.queue2) > 0:
            el2 = self.queue2.popleft()
            self.queue1.append(el2)            

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queue1.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue1[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()