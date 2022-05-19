def get_guess():
    alpha = False
    while not alpha:
        guess = input("What letter would you like to guess? ").lower()
        if guess.isalpha() and len(guess) > 0:
            alpha = True
        else:
            print("Please enter a valid, alphabetic guess.")
    return guess

def get_final_guess():
    y_n = ['n','y','no','yes','kill']
    valid = False
    while not valid:
        final_guess = input("Is this your final guess? (y/n) ").lower()
        if final_guess in y_n:
            valid = True
        else:
            print("Please enter y or n.")
    return final_guess


word_list = ['baboon', 'cat', 'camel', 'ardvark']

hangman_diagram = ["""
  +---+
  |   |
      |
      |
      |
      |
=========
"""
, '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
