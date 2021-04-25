from random import randint
import string

# initial menu for difficulty selection
def menu():
    print("Welcome to the Hangman game, Please select a difficulty level\n")
    print("1 - Easy")
    print("2 - Medium")
    print("3 - Hard\n")

    level = 0

    # repeat the process until we get a valid number
    while level is None or level < 1 or level > 3:
        print("\033[A                             \033[A")

        try:
            level = int(input("-->"))
        except ValueError:
            print("\033[A                             \033[A")
            print("")

    if level == 1:
        return "easy"
    elif level == 2:
        return "medium"
    else:
        return "hard"


def get_guess():
    letter = ''
    while len(letter) != 1 or check_if_alphabet(letter)!= True:
        print("\033[A                             \033[A")
        try:
            letter = input("-->")
        except ValueError:
            print("\033[A                             \033[A")
            print("")

    return letter


def check_if_alphabet(letter):
    set_1 = string.ascii_lowercase
    set_2 = string.ascii_uppercase
    is_letter = False
    for i in range(len(set_1)):
        if letter == set_1[i] or letter == set_2[i]:
            is_letter = True
    return is_letter


# function that  returns a word from an array of words
def select_word(word_file):
    # read the file
    my_file = open(word_file)
    # put content in a list
    word_list = my_file.readlines()
    # random selection from a word list
    return word_list[randint(0, len(word_list) - 1)]

    # return the position of the letters if they exist


def letter_checker(letter, word):
    indeces = []

    for i in range(len(word)):
        if letter.lower() == word[i].lower():
            indeces.append(i)
    return indeces


# update the string of underscores to the current guess
def update_output(char_chain, word, indeces):
    done = False
    for i in range(len(indeces)):
        char_chain[indeces[i]] = word[indeces[i]]
    for i in range(len(char_chain)):
        if char_chain[i] == "_":
            done = True
        print(char_chain[i] + " ", end="")
    print("\n")

    return char_chain, done


# displaying the hangman


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
        """
               --------
               |      |
               |      O
               |     /|\\
               |      |
               |     / \\
               -
               """,
        # head, torso, both arms, and one leg
        """
                   --------
                   |      |
                   |      O
                   |     /|\\
                   |      |
                   |     / 
                   -
                """,
        # head, torso, and both arms
        """
                   --------
                   |      |
                   |      O
                   |     /|\\
                   |      |
                   |      
                   -
                """,
        # head, torso, and one arm
        """
                   --------
                   |      |
                   |      O
                   |     /|
                   |      |
                   |     
                   -
                """,
        # head and torso
        """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
        # head
        """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
        # initial empty state
        """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """,
    ]
    return stages[tries]
