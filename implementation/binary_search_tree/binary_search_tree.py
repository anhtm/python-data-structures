"""
Binary Search Tree (BST) implementation:
1. Traversal (inorder, preorder, postorder)
2. Search (recursive & non-recursive)
3. Queries
  - Minimum
  - Maximum
  - Successor
  - Predecessor
4. Insert
5. Delete
"""

class TreeNode:
  def __init__(self, key = None):
    self.key = key
    self.left = None
    self.right = None
    self.p = None

class BinarySearchTree:
  def __init__(self):
    self.root = None

  def inorder(self, node):
    if (node is not None):
      self.inorder(node.left)
      print(node.key, sep=' ')
      self.inorder(node.right)

  def preorder(self, node):
    if (node is not None):
      print(node.key, sep=' ')
      self.preorder(node.left)
      self.preorder(node.right)

  def postorder(self, node):
    if (node is not None):
      self.postorder(node.left)
      self.postorder(node.right)
      print(node.key, sep=' ')

  def search(self, key):
    node = self.root
    while (node is not None and key != node.key):
      if key < node.key:
        node = node.left
      else:
        node = node.right
    return node

  # start node as root
  def recursive_search(self, key, node):
    if (node is None or node.key == key):
      return node
    elif key < node.key:
      return self.recursive_search(key, node.left)
    else:
      return self.recursive_search(key, node.right)

  def get_minimum(self, node):
    while (node.left is not None):
      node = node.left
    return node

  def get_maximum(self, node):
    while (node.right is not None):
      node = node.right
    return node

  def get_successor(self, node):
    if (node.right is not None):
      return self.get_minimum(node.right)
    else:
      parent = node.p
      # Check for parent to have base case to only traverse up to root
      while (parent != None and node == parent.right):
        node = parent
        parent = parent.p
      return parent

  def get_predecessor(self, node):
    if (node.left is not None):
      return self.get_maximum(node.left)
    else:
      parent = node.p
      while (parent != None and node == parent.left):
        node = parent
        parent = parent.p
      return parent

  def insert(self, node):
    current = self.root
    parent = None
    while (current is not None):
      parent = current
      current = current.left if node.key < current.key else current.right
    if (parent is None):
      self.root = node
    else:
      node.p = parent
      if (node.key < parent.key):
        parent.left = node
      else:
        parent.right = node

  def delete(self, node):
    pass

  # TODO: missing parameters
  def transplant(self):
    pass