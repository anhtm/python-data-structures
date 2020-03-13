import sys
sys.path.append('.')

from HashTable import HashTable
from LinkedList.DoublyLinkedList import DoublyLinkedList
from LinkedList.Node import DoublyNode

class DataItem(DoublyNode):
  def __init__(self, key = None, data = None):
    DoublyNode.__init__(self, key)
    self.data = data

class HashTableSC(HashTable):
  """
    Hash Table implementation using Separate Chaining as its collision handling technique
  """

  def hash(self, key):
    return key % 7

  # item: DataItem
  def insert(self, item):
    hashed_value = self.hash(item.key)
    if (self.storage[hashed_value] is None):
      self.storage[hashed_value] = DoublyLinkedList()
    self.storage[hashed_value].append(item)

  # key: DataItem.key
  def search(self, key):
    result = self.storage[self.hash(key)].search(key)
    return result.data if result is not None else result

  def delete(self, item):
    self.storage[self.hash(item.key)].remove(item)

  def print_table(self):
    for item in self.storage:
      if (isinstance(item, DoublyLinkedList)):
        item.print_list()
      else:
        print(item)

def test():
  ht = HashTableSC(5)
  item1 = DataItem(8, 'Hello')
  item2 = DataItem(17, 'How')
  item3 = DataItem(15, 'Are')
  item4 = DataItem(10, 'You')

  ht.insert(item1)
  ht.insert(item2)
  ht.insert(item3)
  ht.insert(item4)
  ht.print_table()
  print("Search result", ht.search(17))
  ht.delete(item3)
  ht.print_table()