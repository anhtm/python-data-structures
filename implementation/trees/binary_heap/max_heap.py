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
    self.storage = []
    self.heap_size = len(self.storage)

  def get_heap_index(self, i):
    return i + 1

  # returns the index of storage[i]'s parent node
  # index needs to start from 1 to remain its correctness
  def parent(self, i):
    return i >> 1
  
  # returns the index of storage[i]'s left child node
  # index needs to start from 1 to remain its correctness
  def left(self, i):
    return i << 1
  
  # returns the index of storage[i]'s left child node
  # index needs to start from 1 to remain its correctness
  def right(self, i):
    return (i << 1) + 1

  """Time complexity: O(log(n))"""
  def max_heapify(self, index):
    #  determine the largest among A[i], A[left(i)] and A[right(i)]
    left_child_i = self.left(index)
    right_child_i = self.right(index)
    largest = None
    if left_child_i < self.heap_size and self.storage[left_child_i] > self.storage[index]:
      largest = left_child_i
    else: largest = index
    if right_child_i < self.heap_size and self.storage[right_child_i] > self.storage[largest]:
      largest = right_child_i
    # Base case: largest is already the index, then max-heap maintains its property
    # hence terminate the execution
    if largest is not index:
      current = self.storage[index]
      # exchange places between the item at current index and the largest item
      self.storage[index] = self.storage[largest]
      self.storage[largest] = current
      self.max_heapify(largest)

  """Time complexity: O(n)"""
  def build_max_heap(self):
    pass

  """Time complexity: O(nlog(n)) """
  def heap_sort(self):
    pass

