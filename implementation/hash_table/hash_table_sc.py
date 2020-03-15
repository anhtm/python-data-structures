import sys
sys.path.append('.')

from implementation.hash_table.hash_table import HashTable
from implementation.linked_list.doubly_linked_list import DoublyLinkedList
from implementation.linked_list.node import DoublyNode

class DataItem(DoublyNode):
  def __init__(self, key = None, data = None):
    DoublyNode.__init__(self, key)
    self.data = data

"""
Hash Table implementation using Separate Chaining as collision handling technique.
It uses DoublyLinkedList as its chaining data structure

Methods:
0. hash: a simple hash function to calculate the index where an item is inserted into
1. insert: insert an item into the hash table
2. search: search for an item by its key
3. delete: delete an item
4. print_table: print all linked list data in the hash table
"""
class HashTableSC(HashTable):
  def hash(self, key):
    return key % 7

  def insert(self, item):
    """
    Time complexity: O(1)
    The worst-case running time for insertion is O(1). The insertion procedure is fast
    in part because it assumes that the element x being inserted is not already present
    in the table (CLRS Chapter 11 pg. 258)
    """
    hashed_value = self.hash(item.key)
    if (self.storage[hashed_value] is None):
      self.storage[hashed_value] = DoublyLinkedList()
    self.storage[hashed_value].push(item)

  def search(self, key):
    """
    Time complexity:
    - Proportional to the length of the list at the key's hashed index
    - Denoted as load factor a = n/m given a hash table T with m slots that stores n elements 
    - The average-case performance of hashing depends on how well the hash function distributes
    the set of keys to be stored among m slots 
    - If the number of hash-table slots is at least proportional to the number of elements in the table,
    we have n = O(m), hence a = n / m = O(m) / m = O(1) (CLRS Chapter 11 pg. 258)
    """
    result = self.storage[self.hash(key)].search(key)
    return result.data if result is not None else result

  def delete(self, item):
    """
    Time complexity: O(1)
    This is under the assumption that hash table uses DoublyLinkedList and not SinglyLinkedList
    """
    self.storage[self.hash(item.key)].remove(item)

  def print_table(self):
    for item in self.storage:
      if (isinstance(item, DoublyLinkedList)):
        item.print_list()
      else:
        print(item)