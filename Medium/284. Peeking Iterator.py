# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        self.myiterator = iterator
        self.cache = None

    def peek(self):
        if self.cache == None:
            self.cache = self.myiterator.next()
            return self.cache
        return self.cache
    def next(self):
        if self.cache:
            temp = self.cache
            self.cache = None
            return temp
        return self.myiterator.next()
        

    def hasNext(self):
        return self.cache != None or self.myiterator.hasNext()

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].