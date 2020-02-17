import sys
sys.path.append("..") # Adds higher directory to python modules path.

from HashTable import HashTable
from LinkedList import DoublyLinkedList

class DataItem:
  def __init__(self, key = None, value = None):
    self.key = key
    self.value = value

class HashTableSC:
  """
    Hash Table implementation using Separate Chaining as its collision handling technique
  """
  def hash(self, key):
    return key % 7

  # item: DataItem object
  def insert(self, item):
    hashed_value = self.hash(item.key)
    slot = self.storage[hashed_value]
    if (slot is None):
      slot = DoublyLinkedList()
      slot.head = item
    else:
      slot.append(item)

  def search(self, key):
    slot = self.storage[self.hash(key)]
    return slot.search(key)


def test():
  ht = HashTableSC()
  ht.insert(DataItem(8, 'Hello'))
  ht.insert(DataItem(17, 'How'))
  ht.insert(DataItem(15, 'Are'))
  ht.insert(DataItem(10, 'You'))
