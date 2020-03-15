import sys
sys.path.append('.')

from implementation.hash_table.hash_table_oa import HashTableOA, CollisionHandler

class TestHashTableOA:
  def test_init(self):
    hash_table_default = HashTableOA()
    assert hasattr(hash_table_default, 'default_size')
    assert hasattr(hash_table_default, 'storage')
    assert hasattr(hash_table_default, 'handle_collision')
  
  def test_get_open_addressing_map(self):
    hash_table_lp = HashTableOA()    
    assert hash_table_lp.handle_collision == hash_table_lp.linear_probe
    hash_table_qp = HashTableOA(CollisionHandler.QUADRATIC_PROBE)
    assert hash_table_qp.handle_collision == hash_table_qp.quadratic_probe
    hash_table_dh = HashTableOA(CollisionHandler.DOUBLE_HASH)
    assert hash_table_dh.handle_collision == hash_table_dh.double_hash

  def test_linear_probe(self):
    hash_table = HashTableOA(CollisionHandler.LINEAR_PROBE)    
    key = 8
    assert hash_table.linear_probe(key, 0) == 1
    assert hash_table.linear_probe(key, 1) == 2

  def test_quadratic_probe(self):
    hash_table = HashTableOA(CollisionHandler.QUADRATIC_PROBE)    
    key = 8
    assert hash_table.quadratic_probe(key, 0) == 1
    assert hash_table.quadratic_probe(key, 1) == 3

  def test_double_hash(self):
    hash_table = HashTableOA(CollisionHandler.DOUBLE_HASH)    
    key = 8
    print(hash_table.double_hash(key, 1))
    assert hash_table.double_hash(key, 0) == 8
    assert hash_table.double_hash(key, 1) == 3

  def test_insert(self):
    hash_table = HashTableOA()
    key = 8    
    hash_table.insert(key)
    assert key in hash_table.storage

  def test_delete(self):
    hash_table = HashTableOA()
    key = 8    
    hash_table.insert(key)
    hash_table.delete(key)
    assert key not in hash_table.storage
    assert hash_table.storage[1] == HashTableOA.DELETED

  def test_search(self):
    hash_table = HashTableOA()
    key = 8
    hash_table.insert(key)
    assert hash_table.search(8) == 1
    assert hash_table.search(10) == None