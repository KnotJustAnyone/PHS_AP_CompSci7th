import random

class Wordle():
    def __init__(self,maxGuesses:int):

        self.answer_list = []
        with open('answers.txt','r',encoding='utf-8') as f:
            for line in f:
                self.answer_list.append(line.strip())
        self.word_list = []
        with open('words.txt','r',encoding='utf-8') as f:
            for line in f:
                self.word_list.append(line.strip())

        self.guesses = 0
        self.maxGuesses = maxGuesses
        self.won = False
        self.answer = self.generateAnswer()
        self.startGame()

    # Should return something like this if successful:
    # ['Green','Green','Yellow','Grey','Grey']
    def guess(self) -> list[str] or None:
        print(f"Guesses left: {6- self.guesses}/{self.maxGuesses}")
        print("----------------------")
        player_guess = input(f"Guess a {len(self.answer)} letter word: ")

        try:
            player_guess = player_guess.lower()
        except:
            print("Error while trying to lower player guess")
            return


        if len(player_guess) != len(self.answer):
            print(f"\nGuess must be {len(self.answer)} letters.\n")
            self.guess()
            return

        if player_guess not in self.word_list:
            print("\nGuess not in word list.\n")
            self.guess()
            return
        
        results = ['' for letter in self.answer]
        found_letters = []

        for index,letter in enumerate(player_guess):
            if letter == self.answer[index]:

                # Prevents case where guessing a letter n times can cause letter to show greater than n times
                # Happens because yellow letter does not check future cases
                if self.answer.count(letter) <= found_letters.count(letter):
                    for i in range(0,index):
                        if results[i] == 'Yellow' and player_guess[i] == letter:
                            found_letters.remove(player_guess[i])
                            results[i] = 'Grey'

                found_letters.append(letter)
                results[index] = 'Green'
            elif self.answer.count(letter) > found_letters.count(letter):
                found_letters.append(letter)
                results[index] = 'Yellow'
            else:
                results[index] = 'Grey'

        self.guesses += 1
        self.displayGuess(player_guess,results)

        return results

    # Should print something like this to the console:
    #  CRANE
    #  🟩🟩🟨⬜⬜
    def displayGuess(self,guess:str,results:str) -> None:
        string = ""
        for result in results:
            if result == 'Green':
                string += '🟩 '
            elif result == 'Yellow':
                string += '🟨 '
            else:
                string += '⬜ '
        guess_print = ""
        for letter in guess:
            guess_print += letter.upper() + ' '

        print(string)
        print(guess_print)

        if guess == self.answer:
            self.won = True

    def generateAnswer(self) -> str:
        return random.choice(self.answer_list)

    # Main game loop, function should end when the game is over
    def startGame(self) -> None:
        while self.guesses < 6 and not self.won:
            self.guess()
        if self.won:
            print(f"You won!\nYou correctly guessed the word {self.answer}.\nGuesses used: {self.guesses}")
        else:
            print(f"You lost.\nThe word was: {self.answer}")

maxGuesses = 6
game = Wordle(maxGuesses)
