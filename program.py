import numpy as np
from random import randint
import os
from helper_functions import *

os.system("cls")


def play(word, lives):
    guess = np.array((len(word) - 1) * ["_"])
    for i in range(len(guess)):
        print(guess[i] + " ", end="")
    print("\n")
    W_guess = []

    # game loop
    guessed = ""
    while guessed != "quit" and lives != 0:
        guessed = get_guess()
        os.system("cls")
        # check if the letter  is valid
        lenght = letter_checker(guessed, word)
        if len(lenght) == 0:
            W_guess.append(guessed)
            print("Wrong guess")
            lives -= 1
            print("remaining lives :", lives)
            print(display_hangman(lives))
            for i in range(len(W_guess)):
                print("Already guessed wrong : ", W_guess[i] + " ", end="\n")

        else:
            print("nice!")
            print("remaining lives :", lives)
            if lives == 7:
                print(display_hangman(6))
            else:
                print(display_hangman(lives))
            for i in range(len(W_guess)):
                print("Already guessed wrong : ", W_guess[i] + " ", end="\n")
        if update_output(guess, word, letter_checker(guessed, word))[1] == False:
            break

    # check if the gussed word  == word
    # pass
    print("GOODBYE, Thanks you for playing!")


def main():
    launch = menu()
    play(select_word(f"countries-and-capitals-level-{launch}.txt"), 7)


main()