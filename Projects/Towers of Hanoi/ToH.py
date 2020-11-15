from stack import Stack

print("\nLet's play Towers of Hanoi!!")


#Create the Stacks
stacks = []
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")
stacks += [left_stack, middle_stack, right_stack]


#Set up the Game
num_disks = int(input("\nHow many disks do you want to play with?\n"))
while num_disks < 3:
  num_disks = int(input("Enter a number greater than or equal to 3\n"))

disks = []
for disk in range(num_disks, 0, -1):
  left_stack.push("Disk" + str(disk))
# left_stack.print_items()
# middle_stack.print_items()
# right_stack.print_items()

num_optimal_moves = (2 ** num_disks) - 1
print("\nThis game can be solved in {0} moves.".format(num_optimal_moves)) 


#Get User Input
def get_input():
  choices = [stack.get_name()[0] for stack in stacks] 
  # choice = input("Select Stack to move: " + str(choices)).format(choices=choices)
  while True:
    user_input = input("Select Stack to move: " + str(choices) + " ").format(choices=choices).upper()

    for i in range(len(stacks)):
      name = stacks[i].get_name()
      letter = choices[i]
      print("Enter {0} for {1}".format(letter, name))

    if user_input in choices:
      for i in range(len(stacks)):
        if user_input == choices[i]:
          print(stacks[i].get_name() + " Stack selected.")
          return stacks[i]

#Play the Game
num_user_moves = 0

while right_stack.get_size() != num_disks:
  print("Move Count: " + str(num_user_moves))
  print("Remaining Optimal Moves: " + str(num_optimal_moves - num_user_moves))
  print("\n...Current Stacks...")
  left_stack.print_items()
  middle_stack.print_items()
  right_stack.print_items()

  while True:

    print("\nWhich stack do you want to move from?\n")
    from_stack = get_input()
    if from_stack.get_size() == 0:
      print("\n\nInvalid move. Try again.")
      break

    print("\nWhich stack do you want to move to?\n")
    to_stack = get_input()
    if to_stack.get_size() == 0 or from_stack.peek() < to_stack.peek():
      move_disk = from_stack.pop()
      to_stack.push(move_disk)
      num_user_moves += 1
    else:
      print( "/n/nInvalid move. Try again.")
    break    
  
  if num_user_moves == num_optimal_moves:
    print("*** Congratulations! ***")
    print("You completed the game in the optimal number of moves.")
  else:
    print("\n\nYou completed the game in {0} moves, and the optimal number of moves is {1}".format(num_user_moves,num_optimal_moves))