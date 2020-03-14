class LinkedList:
  def __init__(self, head = None):
    self.head = head

  def print_list(self):
    temp = self.head
    while (temp):
      print(temp.data, end=' ')
      temp = temp.next
    print('')

  """
  Search for a node based on its data
  Time complexity O(n)
  """
  def search(self, key):
    print("linkedlist::data", key)
    current = self.head
    print("linkedlist::current", current)
    while (current and current.key != key):
      current = current.next
    return current
