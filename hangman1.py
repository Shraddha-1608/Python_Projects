import random
stages = ['''
   +---+
   |   |
   0   |
  /|\  |
  / \  |
       |
========
''', '''
   +---+
   |   |
   0   |
  /|\  |
  /    |
       |
========
''', '''
   +---+
   |   |
   0   |
  /|\  |
       |
       |
========
''', '''


   +---+
   |   |
   0   |
  /|   |
       |
       |
========
''', '''
   +---+
   |   |
   0   |
   |   |
       |
       |
========
''', '''
   +---+
   |   |
   0   |
       |
       |
       |
========
''']
word_list = ["Avocado", "Apricot", "Blackcurrant", "Blackberry", "Custard Apple", "Curry Berry", "Currant", "Cucumber", "Durian",
             "Dragon fruit", "Feijoa", "Guava", "Huckleberry", "Sapodilla", "Tamarillo", "Tamarind", "Tangerine", "Ugli", "Watermelon"]
chosen_word = (random.choice(word_list)).lower()

list = []
for _ in range(len(chosen_word)):
    list += "_"
print(list)
lives = 5
end_of_game = False
while not end_of_game:
    guess = (input("Guess the letter")).lower()
    if guess in list:
        print(f"You have already gussed ,{guess}")
    print(guess)
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            list[position] = letter

    print(list)
    if "_" not in list:
        end_of_game = True
        print("You win the game")
    print(f"{' '.join(list)}")
    if guess not in chosen_word:
        print(
            f"you have guessed ,{guess}.That's not in the word.You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose the game.")
    print(stages[lives])
