import sys
sys.path.append('.')

from implementation.binary_search_tree.tree_node import TreeNode
from implementation.binary_search_tree.binary_search_tree import BinarySearchTree

class TestBinarySearchTree:
  def test_init(self):
    bst = BinarySearchTree()
    assert hasattr(bst, 'root')

  def get_sample_bst(self):
    bst = BinarySearchTree()
    bst.root = TreeNode(12)
    values = [5, 9, 2, 18, 15, 13, 17, 19]
    for i in values:
      bst.insert(TreeNode(i))
    return bst

  def test_recursive_search(self):
    bst = self.get_sample_bst()
    assert bst.recursive_search(18, bst.root) is not None
    assert bst.recursive_search(100, bst.root) is None

  def test_search(self):
    bst = self.get_sample_bst()
    assert bst.search(18) is not None
    assert bst.search(100) is None

  def test_get_minimum(self):
    bst = self.get_sample_bst()
    assert bst.get_minimum(bst.root).key == 2

  def test_get_maximum(self):
    bst = self.get_sample_bst()
    assert bst.get_maximum(bst.root).key == 19

  def test_get_successor(self):
    bst = self.get_sample_bst()
    assert bst.get_successor(bst.search(12)).key == 13
    assert bst.get_successor(bst.search(17)).key == 18

  def test_get_predecessor(self):
    bst = self.get_sample_bst()
    assert bst.get_predecessor(bst.search(13)).key == 12
    assert bst.get_predecessor(bst.search(18)).key == 17

  def test_insert(self):
    bst = BinarySearchTree()
    bst.insert(TreeNode(12))
    assert bst.root.key == 12
    bst.insert(TreeNode(15))
    assert bst.root.right.key == 15
    assert bst.root.right.p.key == 12
    bst.insert(TreeNode(3))
    assert bst.root.left.key == 3
    assert bst.root.left.p.key == 12

  def test_transplant(self):
    pass

  def test_delete(self):
    pass



