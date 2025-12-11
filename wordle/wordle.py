import random

class Wordle():
    def __init__(self,maxGuesses):

        self.answer_list = []
        with open('wordle/answers.txt','r',encoding='utf-8') as f:
            for line in f:
                self.answer_list.append(line.strip())
        self.word_list = []
        with open('wordle/words.txt','r',encoding='utf-8') as f:
            for line in f:
                self.word_list.append(line.strip())

        self.guesses = 0 # Amount of times player has guessed
        answer = self.generateAnswer()
        self.startGame(answer,maxGuesses)

    # Must have a string of length 5 passed into it
    # Returns guessResults -> used to display color of the letters
    # guessResults example:
    # ['Green','Green','Yellow','Grey','Grey']
    def guess(self,word):
        pass

    # Returns boolean
    # True if word is in words.txt
    # False otherwise
    def isValidGuess(self,word):
        if word in self.word_list:
            # Returns false if guess is less than 5 letters, just in case
            return len(word) == 5
        return False

    # Does not return
    # guessResults is recieved from guess
    # Should print something like this to the console:
    #  CRANE
    #  🟩🟩🟨⬜⬜
    def displayGuess(self,guessResults):
        pass

    # Returns a string of length 5, taken from words.py
    def generateAnswer(self):
        return random.choice(self.answer_list)

    # Does not return
    # word is a word generated from generateWord()
    # maxGuesses is an int that determines how many guesses the player gets
    # Main game loop, function should end when the game is over
    def startGame(self,word,maxGuesses):
        pass