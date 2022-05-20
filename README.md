# hangman

## Here we have two implementations of the hangman game, hangman, and the combination of files new_game.py and hangman_help.py, which is newer and more concise.

## We take randomly take a word from our stored words in hangman_help.py

## The new_game.py implementation consists of a while loop while prompts for user input of a guess. We first check to see if the guess has been guessed before by comparing it to our stored guesses in a set.

## If our guess is more than one character long, it may be our final guess for the word. We get user input if the guess is our final. If it is, we check to see if it correct, and assign a win or lose. 

## If the guess is one character, we check to see if that letter is in our word, and replace the corresponding blanks with the letter. If it is not, we lose a life and iterate our hangman_diagram from hangman_help.py. If our blank array is the same as our word, we win. If we run out of lives, we lose.

# Our hangman_help.py file includes some functions to get a guess and if our guess is final or not.
