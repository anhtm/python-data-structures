import sys
sys.path.append('.')

from implementation.trees.tree_node import TreeNode

"""
A binary search tree is a binary tree in which every node fits a specific ordering property: 
all left descendents <= n < all right descendents. This must be true for each node n.

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

  """
  Time complexity: O(1)
  """
  def transplant(self, node, new_node):
    # node is root
    if (node.p == None): 
      self.root = new_node
    elif (node.p.left == node):
      node.p.left = new_node
    else:
      node.p.right = new_node
    if (new_node != None):
      new_node.p = node.p

  """
  Time complexity: O(h) where h is the height of the tree
  BST is a binary tree, so the time to traverse the tree is O(log(n)), where n is the number of nodes in the tree
  """
  def delete(self, node):
    if (node.left == None):
      self.transplant(node, node.right)
    elif (node.right == None):
      self.transplant(node, node.left)
    else:
      # successor is always in node's right subtree, since its right subtree is not None
      successor = self.get_successor(node)
      if (node.right != successor):
        # successor does not have a left child, since it's already the smallest item of node's right subtree
        self.transplant(successor, successor.right)
        successor.right = node.right
        successor.right.p = successor
      # This is handled in both cases: where successor is or is not node's right child
      self.transplant(node, successor)
      successor.left = node.left
      successor.left.p = successor 