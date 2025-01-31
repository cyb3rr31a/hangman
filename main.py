# A Simple Hangman Game.

import random
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo

lives = 6

print(logo)

chosen_word = random.choice(word_list)
print(f"The word is {chosen_word}.")

placeholder = ""

for letter in chosen_word:
    placeholder += "_"

print(placeholder)

gameover = False

correct_guesses = []

while not gameover:

    print(f"********************{lives}/6 LIVES LEFT********************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_guesses:
        print(f"You've already guessed {guess}.")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_guesses.append(guess)
        elif letter in correct_guesses:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"{guess} is not in the word. You lose a life.")
        if lives == 0:
            gameover = True
            print(f"*******It was {chosen_word}. You lose!*******")

    if display == chosen_word:
        gameover = True
        print("***************You win!**************")

    print(stages[lives])