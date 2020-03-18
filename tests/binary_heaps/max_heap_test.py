import sys
sys.path.append('.')

from implementation.trees.binary_heap.max_heap import MaxHeap
from implementation.trees.tree_node import TreeNode

class TestMaxHeap:

  storage = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]

  def test_node(self):
    max_heap = MaxHeap()
    max_heap.storage = TestMaxHeap.storage
    max_heap.heap_size = len(TestMaxHeap.storage)
    assert max_heap.parent(2) == 1
    assert max_heap.left(2) == 4
    assert max_heap.right(2) == 5

  def test_max_heapify(self):
    pass


  


