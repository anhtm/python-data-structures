from LinkedListBase import LinkedListBase
from Node import Node

class SinglyLinkedList(LinkedListBase):
  """
  @description Insert a node at the beginning of the linked list
  @analysis
    - Time complexity O(1)
  """
  def push(self, node):
    temp = self.head
    self.head = node # node is now head
    node.next = temp # and the previous head is now the second node in the chain
  
  """
  @description Insert a node at the end of the linked list
  @analysis
    - Time complexity O(n)
  """
  def append(self, node):
    if (self.head is None):
      self.head = node
    else:
      tail = self.get_tail()
      tail.next = node

  """
  @description Get the last node of the linked list
  @analysis
    - Time complexity O(n): It has to traverse the whole list to find the tail node
  """
  def get_tail(self):
    temp = self.head
    while (temp is not None and temp.next is not None):
      temp = temp.next
    return temp
  
  """
  @description Insert a node after another node. This assumes that prev_node exists in the linked list
  @analysis
    - Time complexity O(1)
  """
  def insert_after(self, prev_node, new_node):
    temp = prev_node.next
    prev_node.next = new_node
    new_node.next = temp

  """
  @description Remove a node from the linked list
  @analysis
    - Time complexity O(n)
  """
  def remove(self, node):
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

test_singly_linked_list()

