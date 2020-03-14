import sys
sys.path.append('.')

from implementation.hash_table.hash_table import HashTable

class TestHashTable:
  def test_init_default(self):
    hash_table_default = HashTable()
    assert hasattr(hash_table_default, 'default_size')
    assert hasattr(hash_table_default, 'storage')
    assert hash_table_default.default_size == 13
    assert len(hash_table_default.storage) == 13

  def test_init_custom(self):
    hash_table_custom = HashTable(2)
    assert hasattr(hash_table_custom, 'default_size')
    assert hasattr(hash_table_custom, 'storage')
    assert hash_table_custom.default_size == 2
    assert len(hash_table_custom.storage) == 2
