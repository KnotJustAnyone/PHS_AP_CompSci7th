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

    def wordle_guess(self, guess):
        """
        Takes a 5-letter guess and returns a list:
        ['green', 'yellow', 'gray', ...]
        """
        guess = guess.lower()
        result = ["gray"] * 5

        # Make editable copies
        secret_list = list(self.secret_word)
        guess_list = list(guess)

        # FIRST PASS: Check greens
        for i in range(5):
            if guess_list[i] == secret_list[i]:
                result[i] = "green"
                secret_list[i] = None  # Remove matched letter

        # SECOND PASS: Check yellows
        for i in range(5):
            if result[i] == "gray" and guess_list[i] in secret_list:
                result[i] = "yellow"
                secret_list[secret_list.index(guess_list[i])] = None

        return result

    def display_wordle_result(self, guess, result):
        """
        Prints emojis for Wordle result.
        """
        emoji_map = {
            "green": "🟩",
            "yellow": "🟨",
            "gray": "⬛"
        }

        display = ""
        for r in result:
            display += emoji_map[r]

        print(f"{guess.upper()}  ->  {display}")

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

