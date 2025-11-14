# Word Guessing Game Prototype
# Green Team Member: Noah Tsui (Group Leader), Aldo Ortiz
#Class outline for a Word Guessing Game.
# Aldo: It includes variables and functions but no actual working code yet.

import random

class WordGuessingGame:

    # Step 3 (Major Component assignment) - Aldo:
    # A list of possible words the game can choose from.
    # This component is needed for the choose_word function to work.
    word_list = ["apple", "banana", "grape", "orange", "melon"]

    def __init__(self):
        # Noah:  secret word that the player tries to guess
        self.secret_word = ""
        # Noah: A list of letters the player has already guessed
        self.guessed_letters = []
        # Noah: How many tries the player has left
        self.tries_left = 6
        # Noah: The word displayed to the player with blanks for missing letters
        self.display_word = ""
        # Noah: Boolean value to track if the game is still active
        self.game_over = False

    # Step 1 (Function Progress) - Aldo:
    def choose_word(self):

        # Picks a random word from the word list and sets it as the secret word.
        # Also sets up the blank display word.
        self.secret_word = random.choice(self.word_list)
        self.display_word = "_" * len(self.secret_word)
        print("A secret word has been chosen.")
        return None


    def guess_letter(self, letter):

        #Aldo: Checks if the guessed letter is in the secret word.
        return None

    def restart_game(self):

        #Noah: Resets all variables to start a new game.
        return None

# Step 2 (Test) - Noah:
# Simple test to check if the choose_word function selects a word
def test_choose_word():
    game = WordGuessingGame()
    game.choose_word()
    # Print the secret word to confirm it was chosen
    print("Testing choose_word(): Secret word is", game.secret_word)
    # Check the display word has the same number of blanks
    print("Display word looks like:", game.display_word)
    print("Test complete.")

# End of WordGuessingGame class

test_choose_word()
