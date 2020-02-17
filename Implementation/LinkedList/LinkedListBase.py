class LinkedListBase:
  def __init__(self, head = None):
    self.head = head

  def print_list(self):
    temp = self.head
    while (temp):
      print(temp.data)
      temp = temp.next

  def get_tail(self):
    if (self.head is None):
      return None
    temp = self.head
    while (temp.next is not None):
      temp = temp.next
    return temp

  def search(self, node):
    temp = self.head
    while (temp):
      if (temp == node):
        return node
      else:
        temp = temp.next
    return None
