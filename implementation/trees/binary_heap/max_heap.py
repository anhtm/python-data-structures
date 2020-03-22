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
    # heap size does not exceed len(self.storage) and 
    # does not always equal to len(self.storage)
    self.heap_size = len(self.storage) 
    self.heap = []

  """
  Return the index of node i's parent.
  """
  @staticmethod
  def parent(i):
    return int((i - 1) / 2)
  
  """ Return the index of node i's left child  """
  @staticmethod
  def left(i):
    return int(i * 2 + 1)
  
  """ Return the index of node i's right child  """
  @staticmethod
  def right(i):
    return int(i * 2 + 2)

  """
  Time complexity: O(log(n))
  """
  def max_heapify(self, index):
    list_left_i = MaxHeap.left(index)
    list_right_i = MaxHeap.right(index)
    largest = None
    #  determine the largest among A[i], A[left(i)] and A[right(i)]
    if list_left_i < self.heap_size and self.storage[list_left_i] > self.storage[index]:
      largest = list_left_i
    else: largest = index
    if list_right_i < self.heap_size and self.storage[list_right_i] > self.storage[largest]:
      largest = list_right_i
    if largest is not index:
      # exchange places between the item at current index and the largest item
      self.exchange(index, largest)
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
      # swap item at current index with the largest item (which is at the 1st index of list)
      self.exchange(i, 0)
      self.heap_size -= 1
      self.max_heapify(0)

  """Swap values at index a and b. Assume that these values exist in storage"""
  def exchange(self, a, b):
    temp_a = self.storage[a]
    self.storage[a] = self.storage[b]
    self.storage[b] = temp_a

  """Time complexity: O(1) - assuming that the list is already a max heap"""
  def maximum(self):
    return self.storage[0]

  def extract_max(self):
    if (self.heap_size < 1):
      raise Exception("Heap underflow")
    max = self.maximum()
    # swap last with first item
    self.exchange(self.heap_size - 1, 0)
    self.heap_size -= 1
    self.max_heapify(0)
    return max
    
  def insert(self, key):
    pass

  """Increase the value at index i with new_value"""
  def increase_key(self, i, new_value):
    if new_value < self.storage[i]:
      raise Exception("New value is not valid. Should be at least", self.storage[i])
    self.storage[i] = new_value
    # Increase key would potentially break max heap property.
    # Compare node with its parent until max heap property is preserved
    # Add check for i > 1 since if i == 1 => storage[i] is max, hence parent(i) is not valid
    while (i > 1 and self.storage[MaxHeap.parent(i)] < self.storage[i]):
      self.exchange(self.parent(i), i)
      i = self.parent(i)