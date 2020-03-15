import sys
sys.path.append('.')

from implementation.linked_list.linked_list import LinkedList
from implementation.linked_list.node import Node

"""
Singly Linked List implementation:
1. push: insert a node at the beginning
2. append: insert a node at the end
3. insert_after: insert a node after another node
4. get_tail: get the last node in the linked list
5. remove: remove a node from the linked list
"""

class SinglyLinkedList(LinkedList):
  
  def push(self, node):
    """Time complexity: O(1)"""
    temp = self.head
    self.head = node # node is now head
    node.next = temp # and the previous head is now the second node in the chain
  
  def append(self, node):
    """Time complexity: O(n)"""
    if (self.head is None):
      self.head = node
    else:
      tail = self.get_tail()
      tail.next = node

  def get_tail(self):
    """Time complexity: strict O(n) - Worst/best case scenario is to
    traverse the length of the list to find the tail"""
    temp = self.head
    while (temp is not None and temp.next is not None):
      temp = temp.next
    return temp
  
  def insert_after(self, prev_node, new_node):
    """Time complexity: O(1)"""
    temp = prev_node.next
    prev_node.next = new_node
    new_node.next = temp

  def remove(self, node):
    """Time complexity: O(n)"""
    if (self.head == node):
      self.head = node.next
    else:
      current = self.head.next
      prev = self.head
      while (current):
        if (current == node):
          # connect previous node with the next one, leaving the one to be removed out of the chain
          prev.next = current.next
          break
        else:
          prev = current
          current = current.next