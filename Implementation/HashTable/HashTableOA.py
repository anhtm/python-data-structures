from HashTable import HashTable

class HashTableOA(HashTable):
  """
    Hash Table implementation using Open Addressing as its collision handling technique
    There are 3 available options that can be chosen during instantiation: 
      - linear_probe (Linear Probing)
      - quadratic_probe (Quadratic Probing)
      - double_hash (Double Hashing)
    If omitted, defaults to linear_probe
  """
  
  DELETED = 'DELETED'

  def __init__(self, collision_handler = None, default_size = 13): # choose m length of list to be a prime number
    HashTable.__init__(self, default_size)
    if (collision_handler is None):
      self.handle_collision = self.get_open_addressing_method('linear_probe')
    else:
      self.handle_collision = self.get_open_addressing_method(collision_handler)

  def get_open_addressing_method(self, method_name):
    if (method_name == "linear_probe"):
      return self.linear_probe
    elif (method_name == "quadratic_probe"):
      return self.quadratic_probe
    elif (method_name == "double_hash"):
      return self.double_hash
    else:
      return None
  
  def general_hash(self, key):
    return key % 7

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

  def quadratic_probe(self, key, probe):
    """
      Quadratic Probing uses the following formula:
        h(k, i) =  (h'(k) + c1 * i + c2 * i^2) % m (CLRS Chapter 11)
        where:
          c1 and c2 are positive auxiliary constants
        to make full use of the hash table, the values of c1, c2, and m are constrained
    """
    return (self.general_hash(key) + probe + probe**2) % len(self.storage)

  def double_hash(self, key, probe):
    """
      Double hashing uses the following formula:
        h(k, i) =  (h1(k) + i * h2(k)) % m (CLRS Chapter 11)
        where:
          h1 and h2 are auxiliary hash functions
        to make full use of the hash table, the values of c1, c2, and m are constrained
    """
    return (self.hash_1(key) + probe * self.hash_2(key)) % len(self.storage)

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
      # If the slot is empty
      if (slot_value is None or slot_value == self.DELETED):
        self.storage[hashed_key] = data
        return hashed_key # returns the index at which data is stored
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


def test(method_name, table_size = 13):
  print('Hash table: %s' % method_name)
  ht = HashTableOA(method_name, table_size)

  ht.insert(8)
  ht.insert(17)
  ht.insert(15)
  ht.insert(10)
  ht.print_table()

  ht.delete(8)
  ht.print_table()

  ht.insert(22)
  ht.print_table()

test('linear_probe')
test('quadratic_probe')
test('double_hash')
test('linear_probe', 3)

