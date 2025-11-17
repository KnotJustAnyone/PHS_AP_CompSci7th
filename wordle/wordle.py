import random

class Wordle():
    def __init__(self,maxGuesses):
        self.guesses = 0 # Amount of times player has guessed
        word = self.generateWord()
        self.startGame(word,maxGuesses)

    # Must have a string of length 5 passed into it
    # Returns guessResults -> used to display color of the letters
    # guessResults example:
    # ['Green','Green','Yellow','Grey','Grey']
    def guess(self,word):
        pass

    # Does not return
    # guessResults is recieved from guess
    # Should print something like this to the console:
    #  CRANE
    #  🟩🟩🟨⬜⬜
    def displayGuess(self,guessResults):
        pass

    # Returns a string of length 5, taken from words.py
    def generateWord(self):
        word_list = []
        with open('wordle/words.txt','r',encoding='utf-8') as f:
            for line in f:
                word_list.append(line.strip())
        return random.choice(word_list)

    # Does not return
    # word is a word generated from generateWord()
    # maxGuesses is an int that determines how many guesses the player gets
    # Main game loop, function should end when the game is over
    def startGame(self,word,maxGuesses):
        pass