class LinkedList:
  def __init__(self, head = None):
    self.head = head

  def print_list(self):
    temp = self.head
    while (temp):
      info = temp.data if hasattr(temp, 'data') else temp.key
      print(info, end=' ')
      temp = temp.next
    print('')

  def search(self, key):
    """
    Search for a node based on its data
    Time complexity O(n)
    """
    current = self.head
    while (current and current.key != key):
      current = current.next
    return current
