import sys
sys.path.append('.')

from implementation.linked_list.linked_list import LinkedList
from implementation.linked_list.node import Node

class SinglyLinkedList(LinkedList):
  
  def push(self, node):
    """
    Insert a node at the beginning of the linked list
    Time complexity O(1)
    """
    temp = self.head
    self.head = node # node is now head
    node.next = temp # and the previous head is now the second node in the chain
  
  def append(self, node):
    """
    Insert a node at the end of the linked list
    Time complexity O(n)
    """
    if (self.head is None):
      self.head = node
    else:
      tail = self.get_tail()
      tail.next = node

  def get_tail(self):
    """
    Get the last node of the linked list
    Time complexity O(n): Need to traverse the whole list to find the tail node
    """
    temp = self.head
    while (temp is not None and temp.next is not None):
      temp = temp.next
    return temp
  
  def insert_after(self, prev_node, new_node):
    """
    Insert a node after another node. 
    Time complexity O(1)

    prev_node -- this node is assumed to exist
    new_node  -- the node to be inserted into
    """
    temp = prev_node.next
    prev_node.next = new_node
    new_node.next = temp

  def remove(self, node):
    """
    Remove a node from the linked list
    Time complexity O(n)
    """
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

def test_singly_linked_list():
  node_1 = Node(1)
  node_2 = Node(2)
  node_3 = Node(3)
  node_4 = Node(4)
  node_5 = Node()
  node_6 = Node(6)

  linked_list = SinglyLinkedList()
  linked_list.push(node_1)
  linked_list.append(node_2)
  linked_list.append(node_3)
  linked_list.push(node_4)
  linked_list.append(node_5)
  linked_list.insert_after(node_4, node_6)
  linked_list.print_list()

  assert linked_list.head == node_4

  linked_list.remove(node_2)
  assert not linked_list.search(node_2)

