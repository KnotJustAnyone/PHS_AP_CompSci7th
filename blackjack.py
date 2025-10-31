import random #for shuffling
import time #for deleting lines
countdown = 10
from deck_of_cards import Deck
players = [] #players
round1 = False

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
deck = Deck(False, True, True, 6)
deck.shuffle()

class Player: #player properties
    def __init__(self,name,money=1500): #creating player, give money
        self.name = name #player name, may not use because they'll see each other's cards?
        self.hand = [] #hand of cards
        self.money = money #money amount
        self.bet = 0 #bet amount
        self.insbet = 0 #insurance bet amount
    
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
        for player in players:
            if len(player.hand) == 2 and player.hand[0][1] == player.hand[1][1]:
                while True:
                    ifsplit = input(f"Would {player.name} like to split your hand? (y or n)? ").strip().lower()
                    if ifsplit in ("y", "n"):
                        break
                    print("y or n please")
                if ifsplit == "y":
                    splitcard = player.hand.pop() 
                    player.newcard(1)  
                    splitplayer = Player(f"{player.name} Split", player.money)
                    splitplayer.hand = [splitcard]
                    splitplayer.bet = player.bet
                    player.money -= player.bet
                    splitplayer.newcard(1)
                    players.append(splitplayer)
                    print(f"{player.name} has 2 hands.")
                    return True
            return None

    def doubledown(self):
        currenttot = 0
        for player in players:
            if len(player.hand) == 2:
                for i in player.hand:
                    currenttot += card_value(i)
                if currenttot == 9 or currenttot == 10 or currenttot == 11:
                    while True:
                        ifdouble = input(f"Would {player.name} like to double down? (y or n)?").strip().lower()
                        if ifdouble in ("y", "n"):
                            break
                        print("y or n please")
                    if ifdouble == "y":
                        player.newcard(1)
                        player.bet = player.bet * 2
                        return True
                return None
            return None

    def insurance(self, dealer):
        insuranceT = False
        dealer = Dealer(players)
        if card_value(dealer.dealerhand[0]) == 11 and round1 == True:
            for player in players:
                while True:
                    ifins = input(f"Would {player.name} like insurance (y or n)?").strip().lower()
                    if ifins in ("y","n"):
                        break
                    print("y or n please")
                if ifins == "y":
                    insuranceT = True
                    while True:
                        ins = int(input(f"How much would {player.name} like in the side bet?"))
                        if ins <= 0.5 * player.bet and ins > 0 and type(ins) == int:
                            break
                        print("It must be under half your original bet and higher than 0.")
                    player.insbet = ins
                    player.money -= ins
                    print(f"{player.name} has put ${player.insbet} in the side bet!")
            if insuranceT == True:
                insuranceT = False
                print(f"The dealer reveals his second card as... {dealer.dealerhand[1]}")
                if card_value(dealer.dealerhand[1]) == 10:
                    for player in players:
                        if player.insbet > 0:
                            print(f"Player makes 2x their side bet, {player.insbet}!")
                            player.bet += player.insbet * 2
                            player.insbet = 0
                else:
                    print("All insurance bets are lost!")
                    for player in players:
                        player.insbet = 0
    
class Dealer: #dealer properties
    def __init__(self, players): #creating dealer + what its actions will be
        self.deck = Deck(False, True, True) #taking deck
        #is it just self.deck = deck?
        self.players = players #taking players
        self.dealerhand = [] #dealer's hand of cards

    def deal1(self): #first deal for all players
        for player in self.players:
            player.newcard(2)
            print(f"{player.name}'s cards: \033[1m{deck.identify_card(player.hand[0])}, {deck.identify_card(player.hand[1])}\033[0m")
        self.dealerhand = self.deck.deal(2)
        round1 = True

    def dealershow(self): #dealer shows one card
        print(f"The Dealer reveals a card: {self.dealerhand[0]}.")
    
    def round(self): #player: hit or stand, if over 21, bust
        round1 = False
        pass

    def dealerturn(self): #dealer play, if under 17, will play, if not, will stand
        while self.dealer_value() < 17:
            new_cards = self.deck.deal(1)
            self.dealerhand += new_cards
            print(f"Dealer hits: {new_cards}, hand now: {self.dealerhand}")
        print(f"Dealer stands with: {self.dealerhand}")

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

def splitcheck():
    print("type y to actually test")
    dealer = Dealer(players)
    player = Player("tester")
    players.append(player)
    player.hand = ["h2", "d2"]
    player.splitting()
    print('If "tester has 2 hands." is printed, it should be good. \nPrinting hands now.')
    for playa in players:
        print(f"Player {playa}: {playa.hand}")
    print("Ideally, both players should have one card of the same rank, and another random card.") 

def doubledowncheck():
    print("type y to actually test")
    dealer = Dealer(players)
    player = Player("tester")
    players.append(player)
    player.hand = ["h5","h6"]
    player.bet = 5
    print(f"Player {player}'s hand: {player.hand}, the bet: {player.bet}")
    player.doubledown()
    print(f"Player {player}'s hand: {player.hand}, the bet: {player.bet}")
    print("New hand should have an extra card, net bet should be double the bet.")
    
def test_deal1():
    # Set up test players
    numberOfPlayers = 3
    players = [Player('testplr' + str(i)) for i in range(3)]
    oldPlayerHandLength = [len(player.hand) for player in players]
    # Set up dealer
    dealer = Dealer(players)
    # Test deal 1
    try:
        dealer.deal1()
    except Exception as err:
        print(f"ERROR#########\nUnexpected error occurred! {err}")
        return

    errorOccurred = False
    for index,player in enumerate(players):
        # Each player should have 2 more cards
        if len(player.hand) - oldPlayerHandLength[index] != 2:
            errorOccurred = True
            print(f"ERROR ###########\ndealer.deal1() dealt {len(player.hand) - oldPlayerHandLength[index]} cards, expected 2")
            print(f"Extra info:\nDealer dealt {player.hand} to {player}")
        try:
            results = [card_value(card) for card in player.hand]
        except ValueError:
            errorOccurred = True
            print(f"ERROR ###########\ndealer.deal1() dealt the following cards: {player.hand}, one of which's value could not be determined by card_value()")
    if not errorOccurred:
        print("dealer.deal1 passed all tests")



