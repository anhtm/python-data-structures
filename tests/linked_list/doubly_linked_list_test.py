import sys
sys.path.append('.')

from implementation.linked_list.doubly_linked_list import DoublyLinkedList
from implementation.linked_list.node import DoublyNode

class TestDoublyLinkedList:
  def test_push(self):
    linked_list = DoublyLinkedList()
    linked_list.push(DoublyNode(1))
    assert linked_list.head.key == 1
    assert linked_list.head.prev == None
    assert linked_list.head.next == None
    linked_list.push(DoublyNode(2))
    assert linked_list.head.key == 2
    assert linked_list.head.prev == None
    assert linked_list.head.next.key == 1

  def test_append(self):
    linked_list = DoublyLinkedList()
    for i in range(3): linked_list.append(DoublyNode(i))
    assert linked_list.head.key == 0
    assert linked_list.head.next.key == 1
    assert linked_list.tail.key == 2
    assert linked_list.tail.prev.key == 1

  def test_insert_after(self):
    linked_list = DoublyLinkedList()
    for i in range(3): linked_list.push(DoublyNode(i))
    linked_list.insert_after(linked_list.head, DoublyNode(3))
    new_node = linked_list.head.next
    assert new_node.key == 3
    assert new_node.prev.key == 2
    assert new_node.next.key == 1

  def test_remove(self):
    linked_list = DoublyLinkedList()
    for i in range(3): linked_list.push(DoublyNode(i))
    linked_list.remove(linked_list.head)
    assert linked_list.head.key == 1
    linked_list.remove(linked_list.tail)
    assert linked_list.tail.key == 1