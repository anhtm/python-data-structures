import sys
sys.path.append('.')

from implementation.binary_search_tree.binary_search_tree import BinarySearchTree, TreeNode

class TestBinarySearchTree:
  def test_init(self):
    bst = BinarySearchTree()
    assert hasattr(bst, 'root')

  """ Tree illustration
            12
          /     \
        5         18
      /   \      /  \
    2       9   15   19
          /    /   \
         8    13    17
  """
  def get_sample_bst(self):
    bst = BinarySearchTree()
    bst.root = TreeNode(12)
    values = [5, 9, 2, 18, 15, 13, 17, 19, 8]
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

  def test_transplant_root(self):
    bst = self.get_sample_bst()
    temp = bst.root.right
    bst.transplant(bst.root, bst.root.right)
    assert bst.root == temp
    assert temp.p == None

  def test_transplant_norm(self):
    bst = self.get_sample_bst()
    temp = bst.root.right
    bst.transplant(temp, temp.left)
    assert temp.p.right == temp.left
    assert temp.left.p == temp.p

  # node has no left/right subtree
  def test_delete_case_1(self):
    bst = self.get_sample_bst()
    bst.delete(bst.root.left.left) # delete
    assert bst.root.left.left == None

  # node has left subtree but no right subtree
  def test_delete_case_2(self):
    bst = self.get_sample_bst()
    bst.delete(bst.root.left.right) # delete 9
    assert bst.root.left.right.key == 8

  # node has both left and right subtree, and its successor is its right child
  def test_delete_case_3(self):
    bst = self.get_sample_bst()
    bst.delete(bst.root.right.left) # delete 15, successor = 17
    assert bst.root.right.left.key == 17
    assert bst.root.right.left.left.key == 13
    assert bst.root.right.left.right == None
    assert bst.root.right.left.left.p.key == 17

  # node has both left and right subtree, but its successor is not its right child.
  def test_delete_case_5(self):
    bst = self.get_sample_bst()
    bst.delete(bst.root.left) # delete 5, successor = 8
    assert bst.root.left.key == 8
    assert bst.root.left.left.key == 2
    assert bst.root.left.right.key == 9
    assert bst.root.left.left.p.key == 8
    assert bst.root.left.right.p.key == 8
