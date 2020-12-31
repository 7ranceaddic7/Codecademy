import inspect

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
           "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1,
          3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letters_to_points = {l:p for l,p in zip(letters, points)}
letters_to_points[" "] = 0
print(letters_to_points)
print("\n")

def score_word(word):
  word_score = 0

  for letter in word:
    if letters_to_points[letter] == 1:
      print(f"The letter: \'{letter}\' is worth {letters_to_points[letter]} point.")
    else:
      print(f"The letter: \'{letter}\' is worth {letters_to_points[letter]} points.")
    word_score += letters_to_points[letter]

  return word_score


player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"],
                    "wordNerd": ["EARTH", "EYES", "MACHINE"], 
                    "Lexi Con": ["ERASER", "BELLY", "HUSKY"], 
                    "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

player_to_points = {}
for player, words in player_to_words.items():
  print("\n===== ln" + str(inspect.currentframe().f_lineno) + ", Player: ", end=""); print(player)
  print("===== ln" + str(inspect.currentframe().f_lineno) + ", Player Words: ", end=""); print(words)
  
  player_points = 0
  for word in words:
    word_points = 0
    word_points += score_word(word)
    print("===== ln" + str(inspect.currentframe().f_lineno) + ", Word Score: ", end=""); print(word_points)
    player_points += word_points
    player_to_points[player] = player_points

print("\n===== ln" + str(inspect.currentframe().f_lineno) + ", Player Points: ", end=""); print(player_to_points)

# TODO: Ideas for Practice
# If you want extended practice, try to implement some of these ideas with the Python you’ve learned:

# play_word() — a function that would take in a player and a word, and add that word to the list of words they’ve played
# update_point_totals() — turn your nested loops into a function that you can call any time a word is played
# make your letter_to_points dictionary able to handle lowercase inputs as well
