class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
  def insert(self, value):
    if value <= self.data:
      if self.left == None:
        self.left = Node(value)
      else:
        self.left.insert(value)
    else:
      if self.right == None:
        self.right = Node(value)
      else:
        self.right.insert(value)
  
  def contains(self, value):
    if(value == self.data):
      return True
    elif value < self.data:
      if self.left == None:
        return False
      return self.left.contains(value)
    elif value > self.data:
      if self.right == None:
        return False
      return self.right.contains(value)
  def printInOrder(self):
    if self.left != None:
      self.left.printInOrder()
    print(self.data)
    if self.right != None:
      self.right.printInOrder()
tree = Node(10)
tree.insert(5)
tree.insert(30)
tree.printInOrder()