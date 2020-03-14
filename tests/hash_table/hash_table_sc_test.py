import sys
sys.path.append('.')

from implementation.hash_table.hash_table_sc import HashTableSC, DataItem
from implementation.linked_list.node import DoublyNode
from implementation.linked_list.doubly_linked_list import DoublyLinkedList

class TestDataItem:
  def test_init(self):
    data_item = DataItem()
    assert isinstance(data_item, (DataItem, DoublyNode))
    assert hasattr(data_item, 'key')
    assert hasattr(data_item, 'data')
    assert hasattr(data_item, 'prev')
    assert hasattr(data_item, 'next')

class TestHashTableSC:

  def test_insert(self):
    hash_table = HashTableSC()
    item = DataItem(1, 'hello')
    hash_table.insert(item)
    assert isinstance(hash_table.storage[1], DoublyLinkedList)
    assert hash_table.storage[1].head == item

  def test_insert_multiple(self):
    hash_table = HashTableSC()
    item = DataItem(1, 'hello')
    item2 = DataItem(8, 'world')
    hash_table.insert(item)
    hash_table.insert(item2)
    assert hash_table.storage[1].head == item
    assert hash_table.storage[1].tail == item2

  # TODO: Current test fails. Test DoublyLinkedList.remove
  def test_delete(self):
    hash_table = HashTableSC()
    item = DataItem(1, 'hello')
    item2 = DataItem(8, 'world')
    hash_table.insert(item)
    hash_table.insert(item2)
    hash_table.delete(item)
    assert hash_table.storage[1].head == item2

  def test_search(self):
    hash_table = HashTableSC()
    item = DataItem(1, 'hello')
    item2 = DataItem(8, 'world')
    hash_table.insert(item)
    assert hash_table.search(1) == 'hello'
    assert hash_table.search(8) == None
