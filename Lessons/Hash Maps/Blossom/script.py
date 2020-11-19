from linked_list import Node, LinkedList
from blossom_lib import flower_definitions

import inspect

class HashMap:
  def __init__(self, size):
    self.array_size = size
    self.array = [LinkedList() for item in range(self.array_size)]

  def hash(self, key):
    # print("\n===== ln" + str(inspect.currentframe().f_lineno) + ", [DEBUG INFO]: sum(key.encode()) {0}".format(sum(key.encode())))
    return sum(key.encode())

  def compressor(self, hash_code):
    return hash_code % self.array_size

  def assign(self, key, value):
    array_index = self.compressor(self.hash(key))
    # print("\n===== ln" + str(inspect.currentframe().f_lineno) + ", [DEBUG INFO]: array_index {0}".format(array_index))
    payload = Node([key, value])
    # print("\n===== ln" + str(inspect.currentframe().f_lineno) + ", [DEBUG INFO]: [key, value] {0}".format([key, value]))
    list_at_array = self.array[array_index]
    
    for each in list_at_array:
      # print("\n===== ln" + str(inspect.currentframe().f_lineno) + ", [DEBUG INFO]: each {0}".format(each))
      if each[0] == key:
        each[1] = value
        return
    list_at_array.insert(payload)
  def retrieve(self, key):
    array_index = self.compressor(self.hash(key))
    list_at_index = self.array[array_index]

    for each in list_at_index:
      # print("\n===== ln" + str(inspect.currentframe().f_lineno) + ", [DEBUG INFO]: each[0] {0}".format(each[0]))
      if each[0] == key:
        return each[1]

      else:
        return None


blossom = HashMap(14)
for flower in flower_definitions:
  blossom.assign(flower[0], flower[1])
print("\n===== ln" + str(inspect.currentframe().f_lineno) + ", [DEBUG INFO]: blossom.retrieve {0}".format(blossom.retrieve('wisteria')))