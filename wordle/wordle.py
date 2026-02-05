import random
import datetime

import urllib.request
import json

Settings = {
    'daily': False, # Determines whether the game should choose a seed based off of the current day or not
    'maxGuesses': 6,
    'colorblind': False, # If true, prints direct results instead of colored text
    'wordLength': 6, # Anything other than 5 uses an API, max of 15, min of 2
    'useDictionaryAPI': True # If false, disables the check to see if you guessed a valid word. Doesn't disable the answer generator.
}

RANDOM_WORD_API = 'https://random-word-api.herokuapp.com/word'
DICTIONARY_API = 'https://api.dictionaryapi.dev/api/v2/entries/en/'

class Color:
    GREEN = '\033[32m' 
    YELLOW = '\033[33m' 
    WHITE = '\033[37m'
    RESET = '\033[0m'

def request_data(url):
    try:
        with urllib.request.urlopen(url) as response:
            if response.getcode() == 200:
                data = response.read()
                json_data = json.loads(data.decode('utf-8'))
                return json_data
            else:
                print("Endpoint returned code",response.getcode())
                return None
    except Exception as e:
        print("Exception occurred while getting data",e)
        return None

class Wordle():
    def __init__(self,*,maxGuesses=6,daily=False,colorblind=False,wordLength=5,useDictionaryAPI=True):

        wordLength = min(wordLength,15)
        wordLength = max(2,wordLength)

        self.answer_list = []
        with open('wordle/answers.txt','r',encoding='utf-8') as f:
            for line in f:
                self.answer_list.append(line.strip())
        self.word_list = []
        with open('wordle/words.txt','r',encoding='utf-8') as f:
            for line in f:
                self.word_list.append(line.strip())

        self.guesses = []
        self.results = []

        self.useDictionaryAPI = useDictionaryAPI

        self.maxGuesses = maxGuesses
        self.colorblind = colorblind
        self.won = False

        if wordLength == 5:
            self.answer = self.generateAnswer(daily)
        else:
            print("Calling dictionary API...")
            self.answer = request_data(RANDOM_WORD_API + '?length=' + str(wordLength))[0]

            if not self.answer:
                print("API call failed, defaulting to default word length (5)")
                self.answer = self.generateAnswer(daily)


        self.startGame()

    # Should return something like this if successful:
    # ['Green','Green','Yellow','Grey','Grey']
    def guess(self) -> list[str] or None:
        print(f"Guesses left: {self.maxGuesses - len(self.guesses)}/{self.maxGuesses}")
        print("----------------------")
        player_guess = input(f"Guess a {len(self.answer)} letter word: ")

        try:
            player_guess = player_guess.lower()
        except:
            print("Error while trying to lower player guess")
            self.guess()
            return

        if len(player_guess) != len(self.answer):
            print(f"\nGuess must be {len(self.answer)} letters.\n")
            self.guess()
            return

        if player_guess in self.guesses:
            print("\nAlready guessed word.\n")
            self.guess()
            return

        if len(self.answer) == 5:
            if player_guess not in self.word_list:
                print("\nGuess not in word list.\n")
                self.guess()
                return
        elif self.useDictionaryAPI == True:
            try:
                print("Checking dictionary for guess...")
                print("Requesting:",DICTIONARY_API+player_guess)
                data = request_data(DICTIONARY_API+player_guess)
                
                if data == None:
                    retry = input("DictionaryAPI failed to return data, retry? (y/n):")

                    if 'y' in retry:
                        print("Retrying.")
                        self.guess()
                    else:
                        print("Retrying without API.")
                        self.useDictionaryAPI = False
                        self.guess()
                    return
                
                data[0] # Errors if the API returns a blank table instead of a definition
            except:
                print("Could not find word in dictionary API")
                self.guess()
        
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

        self.guesses.append(player_guess)
        self.results.append(results)
        self.displayGuess(player_guess,results)

        if player_guess == self.answer:
            self.won = True

        return results

    def displayGuess(self,guess:str,results:str) -> None:
        guess_index = self.guesses.index(guess)
        if guess_index > 0:
            self.displayGuess(self.guesses[guess_index - 1],self.results[guess_index - 1])

        if self.colorblind:
            print(results)
            return

        string = ""

        for index,letter in enumerate(guess):
            if results[index] == 'Green':
                string += Color.GREEN + letter.upper() + Color.RESET
            elif results[index] == 'Yellow':
                string += Color.YELLOW + letter.upper() + Color.RESET
            else:
                string += Color.WHITE + letter.upper() + Color.RESET
        
        print(string)

    def generateAnswer(self,daily=False) -> str:
        if daily:
            today = datetime.date.today().isoformat()
            random.seed(today)

        return random.choice(self.answer_list)


    # Main game loop, function should end when the game is over
    def startGame(self) -> None:
        while len(self.guesses) < self.maxGuesses and not self.won:
            self.guess()
        if self.won:
            print(f"You won!\nYou correctly guessed the word {self.answer}.\nGuesses used: {len(self.guesses)}")
        else:
            print(f"You lost.\nThe word was: {self.answer}")

game = Wordle(**Settings)