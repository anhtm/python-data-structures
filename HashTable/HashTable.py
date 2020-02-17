class DataItem:
  def __init__(self, key = None, value = None):
    self.key = key
    self.value = value

class HashTable:
  DELETED = "DELETED"

  def __init__(self, collision_handler = None, default_size = 13): # choose m length of list to be a prime number
    self.default_size = default_size 
    self.storage = [None for i in range (self.default_size)]
    if (collision_handler is None):
      print('Collision handling method is not specified (Available methods: linear_probe, quadratic_probe, double_hash). Defaults to linear_probe')
      self.handle_collision = self.get_open_addressing_method('linear_probe')
    else:
      self.handle_collision = self.get_open_addressing_method(collision_handler)

  def print_table(self):
    print('Hash Table Items:', *self.storage)

  def get_open_addressing_method(self, method_name):
    if (method_name == "linear_probe"):
      return self.linear_probe
    elif (method_name == "quadratic_probe"):
      return self.quadratic_probe
    elif (method_name == "double_hash"):
      return self.double_hash
    else:
      print("Method name is not valid")
      return None
  
  def hash(self, key):
    return key % 7

  def linear_probe(self, key, probe):
    return (self.hash(key) + probe) % len(self.storage)

  def quadratic_probe(self, key, probe):
    return (self.hash(key) + probe + probe**2) % len(self.storage)

  def double_hash(self, key, probe):
    return (self.hash_1(key) + probe * self.hash_2(key)) % len(self.storage)

  def hash_1(self, key):
    return key % len(self.storage)

  def hash_2(self, key):
    return key % (len(self.storage) - 1)
    
  def double_size(self):
    current_size = len(self.storage)
    self.storage.extend([None for i in range (current_size)])
    print("Double size called")
    self.print_table()

  def hash_insert(self, data):
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
    print("Hash table is full. Doubling size, hang in there...")
    self.double_size()
    return self.hash_insert(data)

  def hash_search(self, data):
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

  def hash_delete(self, data):
    self.storage[self.storage.index(data)] = self.DELETED


def test_hash_table(method_name, table_size = 13):
  print('Hash table: %s' % method_name)
  ht = HashTable(method_name, table_size)

  ht.hash_insert(8)
  ht.hash_insert(17)
  ht.hash_insert(15)
  ht.hash_insert(10)
  ht.print_table()

  ht.hash_delete(8)
  ht.print_table()

  ht.hash_insert(22)
  ht.print_table()

test_hash_table('linear_probe')
test_hash_table('quadratic_probe')
test_hash_table('double_hash')

test_hash_table('linear_probe', 3)

