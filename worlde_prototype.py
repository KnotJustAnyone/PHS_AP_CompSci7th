# Word Guessing Game Prototype
# Green Team Member: Noah Tsui (Group Leader), Aldo Ortiz
#Class outline for a Word Guessing Game.
# Aldo: It includes variables and functions but no actual working code yet.

class WordGuessingGame:

    # Aldo: A list of possible words the game can choose from
    word_list = []

    def __init__(self):
        # Noah:  secret word that the player tries to guess
        self.secret_word = ""
        # Noah: A list of letters the player has already guessed
        self.guessed_letters = []
        # Noah: How many tries the player has left
        self.tries_left = 0
        # Noah: The word displayed to the player with blanks for missing letters
        self.display_word = ""
        # Noah: Boolean value to track if the game is still active
        self.game_over = False

    def choose_word(self):
        
        #Aldo: Picks a random word from the word list and sets it as the secret word.
        #Aldo: Also sets up the blank display word.
        
        return None

    def guess_letter(self, letter):
        
        #Aldo: Checks if the guessed letter is in the secret word.
        #Aldo Updates guessed letters and display word.
        
        return None

    def update_display(self):
       
        #Noah: Updates the display word to show letters that have been guessed.

        return None

    def check_win(self):

        #Noah: Checks if the player has guessed the full word.
        #Noah: Returns True or False.

        return None

    def show_status(self):
        
       # Noah: Prints or returns the current state of the game:
       # Noah: display word, guessed letters, and tries left.
        
        return None

    def restart_game(self):
        
        #Noah: Resets all variables to start a new game.
        
        return None

# End of WordGuessingGame class
