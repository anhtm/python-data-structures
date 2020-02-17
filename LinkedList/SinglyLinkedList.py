from LinkedList import LinkedList
from Node import Node

class SinglyLinkedList(LinkedList):

  def push(self, node):
    if (self.head is None):
      self.head = node
    else:
      temp = self.head
      self.head = node # node is now head
      self.head.next = temp # and the previous head is now the second node in the chain
  
  def append(self, node):
    if (self.head is None):
      self.head = node
    else:
      tail = self.get_tail()
      tail.next = node
  
  def insert_after(self, prev_node, new_node):
    if (self.contains(prev_node) is False):
      print("Node is not valid. Hence cannot insert after it")
      return
    temp = prev_node.next
    prev_node.next = new_node
    new_node.next = temp

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
  node_2 = Node(0.5)
  node_3 = Node('hello')
  node_4 = Node(['foo'])
  node_5 = Node()
  node_6 = Node(10000)

  linked_list = SinglyLinkedList()
  linked_list.append(node_1)
  linked_list.append(node_2)
  linked_list.append(node_3)
  linked_list.push(node_4)
  linked_list.insert_after(node_4, node_6)
  linked_list.print_list()

  assert linked_list.head == node_4

  linked_list.remove(node_2)
  assert not linked_list.contains(node_2)
  linked_list.insert_after(node_2, node_6)


test_singly_linked_list()

