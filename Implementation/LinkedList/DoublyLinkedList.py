from LinkedListBase import LinkedListBase
from Node import DoublyNode

class DoublyLinkedList(LinkedListBase):

  def push(self, node):
    if (self.head is None):
      self.head = node
      self.head.prev = None
    else:
      temp = self.head
      self.head = node
      self.head.next = temp
      self.head.next.prev = node # previous head now points to the node as prev

  def append(self, node):
    if (self.head is None):
      self.head = node
    else:
      tail = self.get_tail()
      node.prev = tail
      tail.next = node

  def insert_after(self, prev_node, new_node):
    if (self.search(prev_node) is None):
      print("Node is not in linked list. Hence cannot insert after it")
      return
    temp = prev_node.next
    prev_node.next = new_node
    new_node.prev = prev_node
    new_node.next = temp
    new_node.next.prev = new_node

  def remove(self, node):
    if (self.search(node) is None):
      print("Node is not in linked list. Hence cannot be removed")
      return
    temp_prev = node.prev
    temp_next = node.next
    node.prev.next = temp_next
    node.next.prev = temp_prev


def test_doubly_linked_list():
  node_1 = DoublyNode(1)
  node_2 = DoublyNode(0.5)
  node_3 = DoublyNode('hello')
  node_4 = DoublyNode(['foo'])
  node_5 = DoublyNode('Montreal')
  node_6 = DoublyNode('Toronto >')

  linked_list = DoublyLinkedList()
  linked_list.append(node_1)
  linked_list.append(node_2)
  linked_list.append(node_3)
  linked_list.push(node_4)
  linked_list.push(node_5)
  linked_list.insert_after(node_5, node_6)
  linked_list.print_list()

  assert linked_list.head == node_5

  linked_list.remove(node_2)
  assert not linked_list.search(node_2)

  linked_list.insert_after(node_2, node_6)
  linked_list.print_list()

test_doubly_linked_list()