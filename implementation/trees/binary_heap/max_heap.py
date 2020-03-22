"""
A max-heap is a complete binary tree (that is, totally filled other than the rightmost elements on the last
level) where each node is larger than its children. The root, therefore, is the largest element in the tree.

Max-heap implementation:
- Priority queue implementation:
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
  def __init__(self, storage = []):
    self.storage = storage
    self.heap_size = len(self.storage)

  @staticmethod
  def get_list_index(heap_index):
    return heap_index - 1

  @staticmethod
  def get_heap_index(list_index):
    return list_index + 1

  """
  Return the index of heap[i]'s parent.
  Heap index starts from 1 as opposed to list index which starts from 0
  """
  @staticmethod
  def parent(i):
    return i >> 1
  
  """ Return the index of heap[i]'s left child  """
  @staticmethod
  def left(i):
    return i << 1
  
  """ Return the index of heap[i]'s right child  """
  @staticmethod
  def right(i):
    return (i << 1) + 1

  """
  Time complexity: O(log(n))
  
  index - index of item in list
  """
  def max_heapify(self, index):
    heap_index = MaxHeap.get_heap_index(index)
    left_i = MaxHeap.left(heap_index)
    right_i = MaxHeap.right(heap_index)
    list_left_i = MaxHeap.get_list_index(left_i)
    list_right_i = MaxHeap.get_list_index(right_i)

    largest = None
    #  determine the largest among A[i], A[left(i)] and A[right(i)]
    if left_i <= self.heap_size and self.storage[list_left_i] > self.storage[index]:
      largest = list_left_i
    else: largest = index
    if right_i <= self.heap_size and self.storage[list_right_i] > self.storage[largest]:
      largest = list_right_i
    if largest is not index:
      # exchange places between the item at current index and the largest item
      current = self.storage[index]
      self.storage[index] = self.storage[largest]
      self.storage[largest] = current
      self.max_heapify(largest)

  """Time complexity: O(nlog(n))
  Each call to MAX-max_heapify costs O(n) time, and build_max_heap makes O(n/2) such calls. 
  Thus, the running time is O(nlog(n))
  """
  def build_max_heap(self):
    for i in reversed(range(int(self.heap_size / 2))):
      self.max_heapify(i)

  """Time complexity: O(nlog(n))"""
  def heap_sort(self):
    self.build_max_heap()
    for i in reversed(range(1, len(self.storage))):
      # exchange places between the item at current index and the largest item (which is at the 1st index of list)
      current = self.storage[i]
      self.storage[i] = self.storage[0]
      self.storage[0] = current
      self.heap_size -= 1
      self.max_heapify(0)

  def maximum(self):
    return 
