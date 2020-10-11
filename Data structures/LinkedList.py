class Node:
  def __init__(self, x):
    self.val = x
    self.next = None

class LinkedList:
  head = None
  tail = None
  def __init__(self, x):
    self.head = Node(x)
    self.tail = self.head

  def push(self, x):
    self.tail.next = Node(x)
    self.tail = self.tail.next

  def countList(self):
    cnt = 0
    start = self.head
    while start != None:
      cnt+=1
      start = start.next
    return cnt
    
  def printAll(self):
    curr = self.head
    while curr != None:
      print(curr.val)
      curr = curr.next

linkedList = LinkedList(5)
linkedList.push(15)
linkedList.push(25)
linkedList.push(30)
linkedList.push(35)
linkedList.printAll()