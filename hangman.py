# Word Guessing Game Prototype
# Green Team Member: Noah Tsui (Group Leader), Aldo Ortiz
#Class outline for a Word Guessing Game.
# Aldo: It includes variables and functions but no actual working code yet.
import random
class WordGuessingGame(self):

    # Aldo: A list of possible words the game can choose from
    # A list of possible words the game can choose from.
    # This component is needed for the choose_word function to work.
    word_list = []
    with open('Wordle/words.txt','r',encoding='utf-8') as f:
        for line in f:
            word_list.append(line.strip())

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

    def choose_word(self):

        # Picks a random word from the word list and sets it as the secret word.
        # Also sets up the blank display word.
        self.secret_word = random.choice(self.word_list)
        self.display_word = "_" * len(self.secret_word)
        print("A secret word has been chosen.")
        return None
        
        #Aldo: Checks if the guessed letter is in the secret word.
        #Aldo Updates guessed letters and display word.

    def guess_letter(self, letter):
        # Make sure the input is a single letter
        if len(letter) != 1 or not letter.isalpha():
            print("Please enter a single letter.")
            return

        # Make letter lowercase for consistency
        letter = letter.lower()

        # Check if letter was already guessed
        if letter in self.guessed_letters:
            print("You already guessed that letter!")
            return

        # Add the letter to the list of guessed letters
        self.guessed_letters.append(letter)

        # Check if the guessed letter is in the secret word
        if letter in self.secret_word:
            print(f"Good guess! '{letter}' is in the word.")

            # Reveal the letter(s) in the display_word
            new_display = list(self.display_word)
            for i in range(len(self.secret_word)):
                if self.secret_word[i] == letter:
                    new_display[i] = letter
            self.display_word = "".join(new_display)

            # Check if player has guessed the full word
            if "_" not in self.display_word:
                print(f"Congratulations! You guessed the word: {self.secret_word}")
                self.game_over = True

        else:
            # Wrong guess, lose a try
            self.tries_left -= 1
            print(f"Sorry, '{letter}' is not in the word. You have {self.tries_left} tries left.")

            # Check if player ran out of tries
            if self.tries_left <= 0:
                print(f"Game over! The word was '{self.secret_word}'.")
                self.game_over = True

        
        return None

    def update_display(self): # POSSIBLE REDUNDANCY: show_status()
       
        #Noah: Updates the display word to show letters that have been guessed.

        return None

    def check_win(self): # POSSIBLE REDUNDANCY: var game_over()

        #Noah: Checks if the player has guessed the full word.
        #Noah: Returns True or False.

        return None


    def show_status(self):
        status = (
            f"Word: {' '.join(self.display_word)}\n"
            f"Guessed Letters: {', '.join(self.guessed_letters) if self.guessed_letters else 'None yet'}\n"
            f"Tries Left: {self.tries_left}\n")
        return status

    def restart_game(self):
        option = input ("Do you want to restart the game?")
        if option == "yes":
            self.secret_word = ""
            self.guessed_letters = []
            self.tries_left = 6
            self.display_word = ""
            self.game_over = False
            self.choose_word()
        else:
            print("Continuing game")
        
        return None

# End of WordGuessingGame class

# RUN:
def run_game():
    game = WordGuessingGame()

    while True: # Loop in case of restarts
        game.choose_word()
        
        while True: # Main game loop
            game.update_display() # Redundancy? Will need fixing upon function coding
            game.show_status() # Redundancy? Will need fixing upon function coding
            if game.game_over():
                break

    # Restart?
        print("Would you like to play again? ('y' or 'n')")
        ans = input()
        while not ans.strip().lower() in "yn":
            print("Answer with 'y' or 'n' (without quotation marks). Would you like to play again?")
            ans = input()
        if ans == "y":
            game.restart_game()
        else:
            quit()

run_game()





