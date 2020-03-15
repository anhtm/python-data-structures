import sys
sys.path.append('.')

from implementation.linked_list.linked_list import LinkedList
from implementation.linked_list.node import DoublyNode

"""
Doubly Linked List implementation:
1. push: insert a node at the beginning
2. append: insert a node at the end
3. insert_after: insert a node after another node
4. remove: remove a node from the linked list
"""

class DoublyLinkedList(LinkedList):
  def __init__(self, head = None):
    LinkedList.__init__(self, head)
    self.tail = None

  def push(self, node):
    """Time complexity: O(1)"""
    temp = self.head
    self.head = node
    self.head.prev = None
    self.head.next = temp
    if (temp is not None):
      # previous head now points to the node as prev
      self.head.next.prev = node
    else:
      # node is both head and tail if there is only 1 element in the linked list
      self.tail = node

  def append(self, node):
    """Time complexity: O(1)"""
    if (self.head is None):
      self.head = node
      self.tail = node
    else:
      temp = self.tail
      self.tail = node
      node.prev = temp
      node.prev.next = node

  def insert_after(self, prev_node, new_node):
    """Time complexity: O(1)"""
    temp = prev_node.next
    prev_node.next = new_node
    new_node.prev = prev_node
    new_node.next = temp
    new_node.next.prev = new_node

  def remove(self, node):
    """Time complexity: O(1)"""
    if (node.prev is not None):
      node.prev.next = node.next
    else:
      self.head = node.next
      self.head.prev = None
    if (node.next is not None):
      node.next.prev = node.prev
    else:
      self.tail = node.prev
      self.tail.next = None
