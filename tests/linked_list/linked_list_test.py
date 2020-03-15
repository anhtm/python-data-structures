import sys
sys.path.append('.')

from implementation.linked_list.linked_list import LinkedList

class TestLinkedList:
  def test_init(self):
    linked_list = LinkedList()
    assert hasattr(linked_list, 'head')
