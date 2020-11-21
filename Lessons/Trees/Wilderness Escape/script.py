######
# TREENODE CLASS
######
class TreeNode:
  def __init__(self, story_piece):
    self.story_piece = story_piece

  def add_child(self, child_node):
    self.choices = child_node


######
# VARIABLES FOR TREE
######
story_piece = """
You are in a forest clearing. There is a path to the left.
A bear emerges from the trees and roars!
Do you: 
1 ) Roar back!
2 ) Run to the left...
"""

child_a = """
The bear is startled and runs away.
Do you:
1 ) Shout 'Sorry bear!'
2 ) Yell 'Hooray!'
"""

child_b = """
You come across a clearing full of flowers. 
The bear follows you and asks 'what gives?'
Do you:
1 ) Gasp 'A talking bear!'
2 ) Explain that the bear scared you.
"""


######
# TESTING AREA
######
story_root = TreeNode(story_piece)
story_root.add_child(child_a)
story_root.add_child(child_b)

# user_choice = input("What's your name? ")
# print(user_choice)

print("Once upon a time…")
print(story_root.story_piece)