"""
This is the base class for linked list implementation
This class includes the basic constructor and utility methods as follow:
1. print_list: print list's data|key
2. search: search for a node based on its key
"""

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
    """Time complexity: O(n)"""
    current = self.head
    while (current and current.key != key):
      current = current.next
    return current
