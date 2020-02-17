class Node:
  def __init__(self, data = None):
    self.data = data
    self.next = None

class DoublyNode(Node):
  def __init__(self, data=None):
    Node.__init__(self, data)
    self.prev = None