from heapq import heapify, heappush, heappop 
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.heap = [] 
        heapify(self.heap) 
        self.data = []

    def push(self, x: int) -> None:
        heappush(self.heap, x)
        self.data.append(x)  

    def pop(self) -> None:
        if self.heap[0] == self.data.pop():
            heappop(self.heap)

    def top(self) -> int:
        return self.data[-1]
        
    def getMin(self) -> int:
        return self.heap[0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()