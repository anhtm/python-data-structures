class HashTable:
  def __init__(self, default_size = 13):
    """
    default_size -- the default size of the list when initialized. It should be a prime number
    """
    self.default_size = default_size 
    self.storage = [None for i in range (self.default_size)]

  def print_table(self):
    print('Hash Table Items:', *self.storage)