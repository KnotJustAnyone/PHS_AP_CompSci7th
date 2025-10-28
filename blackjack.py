import random #for shuffling
import time #for deleting lines
countdown = 10
from deck_of_cards import Deck
players = [] #players

class Card: #card properties
    def __init__(self,suit,rank,value): #creating card
        self.suit = suit #suit
        self.rank = rank #rank
        self.value = value #value

def card_value(card): #handle 2-card code to get the value
    if card[1] == "0" or card[1] == "j" or card[1] == "q" or card[1] == "k":
        return 10
    elif card[1] == "1":
        return 11
    elif card[1] in [str(n) for n in range(2,10)]:
        return int(card[1])
    else:
        raise ValueError("Value must be a valid card code. Make sure your card rank is a single digit, or 'j', 'q', or 'k'.")

# Start deck, will need to fix to have value
deck = Deck(False, True, True)
deck.shuffle()

class Player: #player properties
    def __init__(self,name,money=1500): #creating player, give money
        self.name = name #player name, may not use because they'll see each other's cards?
        self.hand = [] #hand of cards
        self.money = money #money amount
        self.bet = 0 #bet amount
    
    def newcard(self, count): #putting card in hand
        self.hand += deck.deal(count)
        
    def resethand(self): #reset hand
        self.hand = []

    def handtotal(self): #total value of cards + will handle ace shenanigans
        total = 0
        for card in self.hand:
            total += card_value(card)
        if total > 21: # Lowers the value of aces to 1 if the total is over 21
            for card in self.hand:
                if card_value(card) == 11:
                    total -= 10 #Should just redo total every time it checks... inefficient, but will work
                    if total <= 21:
                        break
        return total

    def splitting(self):
        if len(self.hand) == 2 and self.hand[0][1] == self.hand[1][1]:
            while True:
                ifsplit = input(f"Would {self.name} like to split your hand? (y or n)? ").strip().lower()
                if ifsplit in ("y", "n"):
                    break
                print("y or n please")
            if ifsplit == "y":
                splitcard = self.hand.pop() 
                self.newcard(1)  
                splitplayer = Player(f"{self.name} Split", self.money)
                splitplayer.hand = [splitcard]
                splitplayer.newcard(1)
                players.append(splitplayer)
                print(f"{self.name} has 2 hands.")
                return True
        return False

                
    
class Dealer: #dealer properties
    def __init__(self, players): #creating dealer + what its actions will be
        self.deck = Deck(False, True, True) #taking deck
        #is it just self.deck = deck?
        self.players = players #taking players
        self.dealerhand = [] #dealer's hand of cards
        self.pot = 0 #money in the pot

    def deal1(self): #first deal for all players
        for player in self.players:
            player.newcard(2)
            print(f"Player {player.name} cards: \033[1m{deck.identify_card(player.hand[0])}, {deck.identify_card(player.hand[1])}\033[0m")
        self.dealerhand = self.deck.deal(2)
        for i in range(countdown, 0, -1):
            print(f"\r\033[4mWrite these cards down, they will be deleted in {i}\033[0m{' ' * 10}", end="", flush=True)
            time.sleep(1)
        print("\033[F\033[K\033[E\033[K", end="", flush=True)
        # F = move cursor up 1 line
        # K = clear to end of line
        # E = move cursor down 1 line (next line)

    def dealershow(self): #dealer shows one card
        print(f"The Dealer reveals a card: {self.dealerhand[0]}.")
    
    def round(self):  # Player: hit or stand, if over 21, bust
    for player in self.players:
        print(f"\n{player.name}'s turn:")
        total = player.handtotal()
        while total <= 21:
            print(f"Hand: {player.hand} (Total: {total})")
            choice = input("Hit or Stand? (h/s): ")
            if choice == 'h':
                player.newcard(1)
                total = player.handtotal()
            elif choice == 's':
                break
            else:
                print("input (h/s).")
        if total > 21:
            print("bust!!")


    def dealerturn(self): #dealer play, if under 17, will play, if not, will stand
        pass

    def dealer_value(self): #dealer total value, will handle aces
        pass

    def check(self): #see if anyone busts or wins or ties
        pass

#Tests: -------------------------------------------------------------------------------------
def resethand_checker():
    testclass = Player("test")
    if testclass.hand == []:
        testclass.hand = [random.randint(0,100000000),1,2,3,4,5,6,7,8,9,"aa"]
        print(testclass.hand)
        print("Hand was given 11 values")
    if testclass.hand != []:
        testclass.resethand()
        print(testclass.hand)
        print("Ran resethand. Hand should be gone.")

def test_hand_total():
    normalTests = [
        [[Card('Hearts','8',8)],8],
        [[Card('Diamonds','Ace',11),Card('Diamonds','Ace',11)],12],
        [[Card('Diamonds','Ace',11),Card('Hearts','9',9),Card('Hearts','9',9)],19],
        [[Card('Spades','Ace',11),Card('Spades','Ace',11),Card('Spades','Ace',11),Card('Spades','Ace',11),Card('Spades','Ace',11),Card('Spades','Ace',11),Card('Spades','Ace',11),Card('Spades','Ace',11)],18],
        [[Card('Diamonds','King',10),Card('Spades','Ace',11)],21],
        [[Card('Diamonds','King',10),Card('Diamonds','King',10),Card('Spades','Ace',11)],21],
    ]
    unexpectedTests = [
        [[],None or 0],
        [[Card('Awesome','Card','Awesome')],None or 0],
        [[[[]]],None or 0],
        [[['A'],['B'],['C'],['D']],None or 0],
    ]
    plr = Player('Tester')
    def evaluateTest(test):
        try:
            plr.hand = test[0]
            result = plr.handtotal()
            expectedResult = test[1]
            if result == expectedResult:
                print("O - Test passed")
            else:
                print(f"X - Test failed, expected {expectedResult} but got {result}")
        except Exception as e:
            print(f"X - Test failed, function returned exception: {e}")
    print("Normal Tests ----- THESE SHOULD ALWAYS PASS")
    for test in normalTests:
        evaluateTest(test)
    print("Unexpected Tests ----- Do not need to pass, the cases tested only happen if other code is cooked")
    for test in unexpectedTests:
        evaluateTest(test)
    
def test_card_deletion():
    playa = Player("testname")
    players = [playa]
    deala = Dealer(players)
    deala.deal1()
    print("If cards or countdown are not gone, this did not work. If so, yay...")


def splitcheck():
    print("type y to actually test")
    dealer = Dealer()
    player = Player("tester")
    player.hand = ["h2", "d2"]
    player.splitting()
    print('If "tester has 2 hands." is printed, it should be good. \nPrinting hands now.')
    for playa in players:
        print(f"Player {playa}: {playa.hand}")
    print("Ideally, both players should have one card of the same rank, and another random card.") 












