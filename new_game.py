import random
import hangman_help as help


word = random.choice(help.word_list)
guesses = set()
lives = 0

blanks = list(word)
for index, letter in enumerate(word):
    if letter != " ":
        blanks[index] = ('_')

active = False
win = 0


while not active:
    lives_left = 6-lives
    print(help.hangman_diagram[lives])
    print(blanks, f"Lives Left: {lives_left}")
    guess = help.get_guess()

    if guess == 'kill':
        break

    if guess in guesses:
        print(f"You've already guessed {guess}! Please guess again. \nPrevious guesses: ", list(guesses), "\n\n")
        print()
        continue

    if len(guess) > 1:
        final_guess = help.get_final_guess()
        if final_guess == "kill":
            break

        if final_guess == 'n' or final_guess == 'no':
            continue
        if word == guess:
            win = True
            active = True
        else:
            win = False
            active = True

    guesses.add(guess)

    if guess not in word:
        lives += 1
    
    if guess in word:
        for index, letter, in enumerate(word):
            if letter == guess:
                blanks[index] = guess

    if blanks == list(word):
        active = True
        win = True

    if lives == 6:
        win = False
        active = True
        print("You've run out of lives.")

    print("\n\n")

    if not active:
        print("Previous guesses: ", list(guesses))

if win == True:
    print("Congratulations! You've won!")
elif win == False:
    print("The word was:", word, "\nYou lose!")
