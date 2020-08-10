import sys
import pytest
sys.path.append('.')

from implementation.heaps.max_heap import MaxHeap
from implementation.trees.tree_node import TreeNode

class TestMaxHeap:

  # Non-max-heap list
  storage = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]

  def test_static_methods(self):
    assert MaxHeap.parent(1) == 0
    assert MaxHeap.left(1) == 3
    assert MaxHeap.right(1) == 4

  def test_max_heapify(self):
    max_heap = MaxHeap([1, 2, 3])
    max_heap.max_heapify(0) # heapify at index 0
    assert max_heap.storage == [3, 2, 1]

  def test_build_max_heap(self):
    max_heap = MaxHeap(TestMaxHeap.storage)
    max_heap.build_max_heap()
    assert max_heap.storage == [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]

  def test_heap_sort(self):
    max_heap = MaxHeap(TestMaxHeap.storage)
    max_heap.heap_sort()
    assert max_heap.storage == [1, 2, 3, 4, 7, 8, 9, 10, 14, 16]

  def test_maximum(self):
    max_heap = MaxHeap(TestMaxHeap.storage)
    max_heap.build_max_heap()
    assert max_heap.maximum() == 16

  def test_extract_max(self):
    max_heap = MaxHeap(TestMaxHeap.storage)
    max_heap.build_max_heap()
    result = max_heap.extract_max()
    assert result == 16
    assert max_heap.heap_size == len(max_heap.storage) - 1

  def test_extract_max_exception(self):
    max_heap = MaxHeap() # storage is empty => should raise an exception
    max_heap.build_max_heap()
    with pytest.raises(Exception):
      max_heap.extract_max()

  def test_increase_key(self):
    max_heap = MaxHeap(TestMaxHeap.storage)
    max_heap.build_max_heap()
    max_heap.increase_key(3, 17)  # increase the value at index 3 to 12
    assert max_heap.maximum() == 17

  def test_increase_key_exception(self):
    max_heap = MaxHeap([1, 2, 3])
    max_heap.build_max_heap()
    with pytest.raises(Exception):
      assert max_heap.increase_key(2, 0) # 0 < 3, hence will raise exception

  def test_insert(self):
    new_val = 5
    max_heap = MaxHeap(TestMaxHeap.storage)
    max_heap.build_max_heap()
    max_heap.insert(new_val)
    assert len(max_heap.storage) == 11
    parent = max_heap.parent(max_heap.storage.index(new_val))
    assert max_heap.storage[parent] > new_val


