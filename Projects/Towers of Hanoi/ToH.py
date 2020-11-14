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
  choice = input("Select Stack to move: " + str(choices)).format(choices=choices)
  while True:
    input("Select Stack to move: " + str(choices) + " ").format(choices=choices)

    for i in range(len(stacks)):
      name = stacks[i].get_name()
      letter = choices[i]
      print("Enter {0} for {1}".format(letter, name))

    user_input = ""

#Play the Game