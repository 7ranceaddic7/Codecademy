load_file_in_context('script.py')

try:
  ll = LinkedList(6)
  ll.insert_beginning(32)
  ll.insert_beginning(-12)
  ll.insert_beginning(48)
  ll.insert_beginning(2)
  ll.insert_beginning(1)
  ll_max = find_max(ll)
  if ll_max != 48:
    fail_tests("For the linked list, `ll`, your `find_max` returned {0} but should have returned 48".format(ll_max))
  ll_2 = LinkedList(60)
  ll_2.insert_beginning(12)
  ll_2.insert_beginning(22)
  ll_2.insert_beginning(-10)
  ll_2_max = find_max(ll_2)
  if ll_2_max != 60:
    fail_tests("For the linked list, `ll_2`, your `find_max` returned {0} but should have returned 60".format(ll_2_max))

  ll_3 = LinkedList("A")
  ll_3.insert_beginning("X")
  ll_3.insert_beginning("V")
  ll_3.insert_beginning("L")
  ll_3.insert_beginning("D")
  ll_3.insert_beginning("Q")
  ll_3_max = find_max(ll_3)
  if ll_3_max != "X":
    fail_tests("For the linked list, `ll_3`, your `find_max` returned {0} but should have returned 'X'".format(ll_3_max))
except AttributeError:
  fail_tests("Make sure you are using the right methods in `LinkedList` and `Node`")

pass_tests()