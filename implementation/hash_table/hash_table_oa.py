import sys
sys.path.append('.')

from enum import Enum
from implementation.hash_table.hash_table import HashTable

class CollisionHandler(Enum):
  LINEAR_PROBE = 1
  QUADRATIC_PROBE = 2
  DOUBLE_HASH = 3

class HashTableOA(HashTable):
  """
  Hash Table implementation using Open Addressing as its collision handling technique
  There are 3 available options that can be chosen during instantiation: 
    - LINEAR_PROBE
    - QUADRATIC_PROBE
    - DOUBLE_HASH
  If omitted, defaults to LINEAR_PROBE
  """
  
  DELETED = 'DELETED'

  def __init__(self, collision_handler = None, default_size = 13): # choose m length of list to be a prime number
    HashTable.__init__(self, default_size)
    self.handle_collision = self.get_open_addressing_map(collision_handler)

  def get_open_addressing_map(self, method):
    mapper = {
      CollisionHandler.LINEAR_PROBE: self.linear_probe,
      CollisionHandler.QUADRATIC_PROBE: self.quadratic_probe,
      CollisionHandler.DOUBLE_HASH: self.double_hash,
    }
    return mapper.get(method, self.linear_probe)

  def linear_probe(self, key, i):
    """
    Linear Probing uses the following formula:
      h(k, i) =  (h'(k) + i) % m (CLRS Chapter 11)
      where:
        k = the key to be hashed
        i = probe sequence
        m = length of the list
    """
    return (self.general_hash(key) + i) % len(self.storage)

  def quadratic_probe(self, key, i):
    """
    Quadratic Probing uses the following formula:
      h(k, i) =  (h'(k) + c1 * i + c2 * i^2) % m (CLRS Chapter 11)
      where:
        k = the key to be hashed
        i = probe sequence
        m = length of the list
        c1 and c2 are positive auxiliary constants
      to make full use of the hash table, the values of c1, c2, and m are constrained
    """
    return (self.general_hash(key) + i + i**2) % len(self.storage)

  def double_hash(self, key, probe):
    """
    Double hashing uses the following formula:
      h(k, i) =  (h1(k) + i * h2(k)) % m (CLRS Chapter 11)
      where:
        h1 and h2 are auxiliary hash functions
      to make full use of the hash table, the values of c1, c2, and m are constrained
    """
    return (self.hash_1(key) + probe * self.hash_2(key)) % len(self.storage)

  def general_hash(self, key):
    return key % 7

  def hash_1(self, key):
    return key % len(self.storage)

  def hash_2(self, key):
    return key % (len(self.storage) - 1)
    
  def double_size(self):
    current_size = len(self.storage)
    self.storage.extend([None for i in range (current_size)])

  def insert(self, data):
    probe_num = 0
    while (probe_num < len(self.storage)):
      hashed_key = self.handle_collision(data, probe_num)
      slot_value = self.storage[hashed_key]
      if (slot_value is None or slot_value == self.DELETED):
        self.storage[hashed_key] = data
        return hashed_key
      else:
        probe_num += 1
    self.double_size()
    return self.insert(data)

  def search(self, data):
    probe_number = 0
    while (probe_number < len(self.storage)):
      hashed_key = self.handle_collision(data, probe_number)
      if (self.storage[hashed_key] == data):
        return hashed_key
      elif (self.storage[hashed_key] is None):
        return None
      else:
        probe_number += 1
    return None

  def delete(self, data):
    self.storage[self.storage.index(data)] = self.DELETED
