"""
A max-heap is a complete binary tree (that is, totally filled other than the rightmost elements on the last
level) where each node is larger than its children. The root, therefore, is the largest element in the tree.

Max-heap implementation:
- Priority queue implementation (All run in O(log(n)) time):
1. insert
2. extract_max
3. increase_key
4. maximum

- Heapsort:
1. max_heapify: maintains a max heap property
2. build_max_heap: produces a maxheap from an unordered input array
3. heapsort: sorts an array in place.
"""

class MaxHeap:
  def __init__(self):
    self.root = None
    self.heap_size = None
    self.storage = []

  """Time complexity: O(log(n))"""
  def max_heapify(self):
    pass

  """Time complexity: O(n)"""
  def build_max_heap(self):
    pass

  """Time complexity: O(nlog(n)) """
  def heap_sort(self):
    pass

