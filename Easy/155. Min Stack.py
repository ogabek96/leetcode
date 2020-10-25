class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minimum = None
        self.data = []

    def push(self, x: int) -> None:
        if self.minimum == None:
            self.minimum = x
        if self.minimum > x:
            self.minimum = x
        self.data.append(x)  

    def pop(self) -> None:
        deleted = self.data.pop()
        if len(self.data) == 0:
            self.minimum = None
            return None
        if self.minimum == deleted:
            self.minimum = self.data[0]
            for d in self.data:
                if self.minimum > d:
                    self.minimum = d

    def top(self) -> int:
        return self.data[-1]
        
    def getMin(self) -> int:
        return self.minimum


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()