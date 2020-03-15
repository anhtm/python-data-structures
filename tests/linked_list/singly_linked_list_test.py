import sys
sys.path.append('.')

from implementation.linked_list.singly_linked_list import SinglyLinkedList
from implementation.linked_list.node import Node

class TestSinglyLinkedList:
  def test_push(self):
    linked_list = SinglyLinkedList()
    linked_list.push(Node(1))
    assert linked_list.head.key == 1
    linked_list.push(Node(2))
    assert linked_list.head.key == 2

  def test_append(self):
    linked_list = SinglyLinkedList()
    for i in range(3): linked_list.append(Node(i))
    assert linked_list.head.key == 0
    assert linked_list.get_tail().key == 2

  def test_get_tail(self):
    linked_list = SinglyLinkedList()
    assert linked_list.get_tail() == None
    for i in range(3): linked_list.push(Node(i))
    assert linked_list.get_tail().key == 0
    assert linked_list.head.key == 2

  def test_insert_after(self):
    linked_list = SinglyLinkedList()
    for i in range(3): linked_list.push(Node(i))
    linked_list.insert_after(linked_list.head, Node(2))
    assert linked_list.head.next.key == 2
    assert linked_list.head.next.next.key == 1

  def test_remove(self):
    linked_list = SinglyLinkedList()
    for i in range(3): linked_list.push(Node(i))
    linked_list.remove(linked_list.head)
    assert linked_list.head.key == 1

  def test_search(self):
    linked_list = SinglyLinkedList()
    assert linked_list.search(1) is None
    linked_list.push(Node(1))
    assert linked_list.search(1) is not None
