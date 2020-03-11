from LinkedListBase import LinkedListBase
from Node import DoublyNode

class DoublyLinkedList(LinkedListBase):
  def __init__(self, head = None):
    LinkedListBase.__init__(self, head)
    self.tail = None

  def push(self, node):
    """
    Insert a node at the beginning of the linked list
    Time complexity O(1)
    """
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
    """
    Insert a node at the end of the linked list
    Time complexity O(1)
    """
    if (self.head is None):
      self.head = node
      self.tail = node
    else:
      temp = self.tail
      self.tail = node
      node.prev = temp
      node.prev.next = node

  def insert_after(self, prev_node, new_node):
    """
    Insert a node after another node. 
    Time complexity O(1)

    prev_node -- this node is assumed to exist
    new_node  -- the node to be inserted into
    """
    temp = prev_node.next
    prev_node.next = new_node
    new_node.prev = prev_node
    new_node.next = temp
    new_node.next.prev = new_node

  def remove(self, node):
    """
    Remove a node from the linked list
    Time complexity O(1)
    """
    temp_prev = node.prev
    temp_next = node.next
    node.prev.next = temp_next
    node.next.prev = temp_prev


def test_doubly_linked_list():
  node_1 = DoublyNode(1)
  node_2 = DoublyNode(2)
  node_3 = DoublyNode(3)
  node_4 = DoublyNode(4)
  node_5 = DoublyNode(5)
  node_6 = DoublyNode(6)

  linked_list = DoublyLinkedList()
  linked_list.append(node_1)
  linked_list.append(node_2)
  linked_list.append(node_3)
  linked_list.push(node_4)
  linked_list.push(node_5)
  linked_list.insert_after(node_4, node_6)
  linked_list.print_list()

  assert linked_list.head == node_5

  linked_list.remove(node_2)
  assert not linked_list.search(node_2)

  linked_list.print_list()

test_doubly_linked_list()