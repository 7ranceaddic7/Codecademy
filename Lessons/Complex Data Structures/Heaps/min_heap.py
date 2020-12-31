class MinHeap:
  def __init__(self):
    self.heap_list = [None]
    self.count = 0

  def add(self, element):
    self.count += 1
    print("\nAdding: {0} to {1}".format(element, self.heap_list))
    self.heap_list.append(element)
    self.heapify_up()

  def retrieve_min(self):
    if self.count == 0:
      print("No items in heap")
      return None
    
    first = self.heap_list[1]
    last = self.heap_list[self.count]
    print("\nRetreiving: {0} from HEAP:{1}".format(first, self.heap_list))

    self.heap_list[1] = last
    self.heap_list.pop()
    self.count -= 1
    print("Last element {0} moved to beginning: {1}".format(last, self.heap_list))    

    self.heapify_down()
    return first

  def heapify_up(self):
    print("\nHeapifying up...")
    print("HEAP: {0}".format(self.heap_list))

    idx = self.count
    swap_count = 0

    while self.parent_idx(idx) > 0:
      parent = self.heap_list[self.parent_idx(idx)]
      child = self.heap_list[idx]

      if parent > child:
        print("Swapping {0} with {1}".format(parent, child))
        swap_count += 1
        self.heap_list[self.parent_idx(idx)] = child
        self.heap_list[idx] = parent

      idx = self.parent_idx(idx)
    print("HEAP RESTORED! {0}".format(self.heap_list))

    element_count = len(self.heap_list)
    if element_count > 3:
      print("Heap of {0} elements restored with {1} swaps".format(element_count, swap_count))
      
  def heapify_down(self):
    idx = 1
    swap_count = 1

    while self.child_present(idx):
      print("\nHEAP: {0}".format(self.heap_list))
      print("Heapifying down...")

      parent = self.heap_list[idx]
      child = self.heap_list[self.get_smaller_child_idx(idx)]

      if parent > child:
        swap_count += 1
        print("Swapping {0} with {1}".format(parent, child))
        self.heap_list[self.get_smaller_child_idx(idx)] = parent
        self.heap_list[idx] = child

      idx = self.get_smaller_child_idx(idx)
    print("HEAP RESTORED! {0}".format(self.heap_list))

    element_count = len(self.heap_list)
    if element_count >= 3:
      print("Heap of {0} elements restored with {1} swaps".format(element_count, swap_count))

  # BEGIN HELPER METHODS
  def parent_idx(self, idx):
    return idx // 2

  def left_child_idx(self, idx):
    return idx * 2

  def right_child_idx(self, idx):
    return idx * 2 + 1

  def child_present(self, idx):
    return self.left_child_idx(idx) <= self.count

  def get_smaller_child_idx(self, idx):
    if self.right_child_idx(idx) > self.count:
      print("There is only a left child")
      return self.left_child_idx(idx)
    else:
      left_child = self.heap_list[self.left_child_idx(idx)]
      right_child = self.heap_list[self.right_child_idx(idx)]
      if left_child < right_child:
        print("Left_child: {0} is smaller than Right_child: {1}".format(left_child, right_child))
        return self.left_child_idx(idx)
      else:
        print("Right_child: {0} is smaller than Left_child: {1}".format(right_child, left_child))
        return self.right_child_idx(idx)
  # END HELPER METHODS
