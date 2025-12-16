import random

class Wordle():
    def __init__(self,maxGuesses:int):

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

    # Should return something like this:
    # ['Green','Green','Yellow','Grey','Grey']
    # should be passed into displayGuess
    def guess(self,word:str) -> list[str]:
        pass

    # Returns True if word is in words.txt
    # else False
    def isValidGuess(self,word:str) -> bool:
        if word in self.word_list:
            # Returns False if guess is less than 5 letters, just in case
            return len(word) == 5
        return False

    # guessResults is recieved from guess
    # Should print something like this to the console:
    #  CRANE
    #  🟩🟩🟨⬜⬜
    def displayGuess(self,guessResults:str) -> None:
        pass

    def generateAnswer(self) -> str:
        return random.choice(self.answer_list)

    # word is a word generated from generateAnswer()
    # Main game loop, function should end when the game is over
    def startGame(self,word:str,maxGuesses:int) -> None:
        pass
    # word is a word generated from generateWord()
    # maxGuesses is an int that determines how many guesses the player gets
    # Main game loop, function should end when the game is over
    def startGame(self,word,maxGuesses):
        pass
