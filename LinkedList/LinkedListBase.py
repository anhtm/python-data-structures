class LinkedListBase:
  def __init__(self, head = None):
    self.head = head

  def print_list(self):
    temp = self.head
    while (temp):
      print(temp.data, end=' ')
      temp = temp.next
    print('')

  """
  @description Search for a node based on its data
  @analysis
    - Time complexity O(n)
  """
  def search(self, data):
    current = self.head
    while (current and current.data != data):
      current = current.next
    return current
