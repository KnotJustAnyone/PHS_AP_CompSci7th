import random
from deck_of_cards import Deck
players = [] #players
round1 = False

def getting_players():
    while True:
        try:
            pnum = int(input("How many players are playing?"))
            break
        except ValueError:
            print("a number (don't use letters) please")
    for i in range(pnum):
        name = input(f"Player {i + 1}'s name: ")
        players.append(Player(name))
    print(f"{pnum} players were added:\n{[pl.name for pl in players]} \n")

def card_value(card): #handle 2-card code to get the value
    if card[1] == "0" or card[1] == "j" or card[1] == "q" or card[1] == "k":
        return 10
    elif card[1] == "1":
        return 11
    elif card[1] in [str(n) for n in range(2,10)]:
        return int(card[1])
    else:
        return None

# Start deck, will need to fix to have value
deck = Deck(False, True, True, 6)
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
        if card_value(dealer.dealerhand[0]) == 11 and round1 == True:
            for player in players:
                while True:
                    ifins = input(f"Would {player.name} like insurance (y or n)?").strip().lower()
                    if ifins in ("y","n"):
                        break
                    print("y or n please")
                if ifins == "y":
                    player.insbet = 0.5 * player.bet
                    player.money -= 0.5 * player.bet
                    print(f"{player.name} has put ${player.insbet} in as insurance!")
                    if card_value(dealer.dealerhand[1]) == 10: 
                        print("Dealer has Blackjack! Insurance bets are doubled and returned.")
                        for player in players:
                            player.money += player.insbet * 2
                            player.insbet = 0
                    else:
                        print("Dealer does NOT have Blackjack, all insurance is lost.")
                        for player in players:
                            player.insbet = 0
    
class Dealer: #dealer properties
    def __init__(self, players): #creating dealer + what its actions will be
        self.players = players #taking players
        self.dealerhand = [] #dealer's hand of cards

    def deal1(self): #first deal for all players
        if len(deck.deck_current) < ((len(players) + 1) * 8): # Ensure enough cards in deck to deal
            deck.shuffle()
        for player in self.players:
            player.newcard(2)
            print(f"{player.name}'s cards: \033[1m{deck.identify_card(player.hand[0])}, {deck.identify_card(player.hand[1])}\033[0m")
        self.dealerhand = self.deck.deal(2)

    def dealershow(self): #dealer shows one card
        print(f"The Dealer reveals a card: {self.dealerhand[0]}.")
    
    def round(self): #player: hit or stand, if over 21, bust
        pass

    def dealerturn(self): #dealer play, if under 17, will play, if not, will stand
        while self.dealer_value() < 17:
            new_cards = deck.deal(1)
            self.dealerhand += new_cards
            print(f"Dealer hits: \033[1m{deck.identify_card(new_cards)}\033[0m, hand now: {self.dealer_value()}")
        print(f"Dealer stands with {self.dealer_value()}")

    def dealer_value(self): #dealer total value, will handle aces
        pass

    def check(self): #see if anyone busts or wins or ties
        pass

#Tests: -------------------------------------------------------------------------------------
def test_getting_players():
    print(f"Your job: attempt {random.randint(2,10)} players.")
    getting_players()
    print('If "5 players were added:\n[array of the names]"\nWas printed, then the code works.')
    
def resethand_checker():
    testclass = Player("test")
    if testclass.hand == []:
        testclass.hand = [random.randint(0,100000000),1,2.3,3,4,False,6,7,None,"None","aa"]
        print(testclass.hand)
        print("Hand was given 11 values")
    if testclass.hand != []:
        testclass.resethand()
        print(testclass.hand)
        print("Ran resethand. Hand should be gone.")

def test_hand_total():
    normalTests = [
        [["h8"],8],
        [["d1","d1"],12],
        [["d1","h9","h9"],19],
        [["s1","s1","s1","s1","s1","s1","d1","d1"],18],
        [["dk","d1"],21],
        [["dk","sk","d1"],21],
    ]
    unexpectedTests = [
        [[],None or 0],
        [["AHHHHHHHHH"],None or 0],
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
    player = Player("tester")
    players.append(player)
    dealer = Dealer(players)
    player.hand = ["h2", "d2"]
    print(f"Current hand: {player.hand}.")
    player.splitting()
    print('If "tester has 2 hands." is printed, it should be good. \nPrinting hands now.')
    for playa in players:
        print(f"Player {playa.name}: {playa.hand}")
    print("Ideally, both players should have one card of the same rank, and another random card.") 

def doubledowncheck():
    print("type y to actually test")
    player = Player("tester")
    players.append(player)
    dealer = Dealer(players)
    player.hand = ["h5","h6"]    print(f"Your job: attempt {random.randint(2,10)} players.")
    getting_players()
    print('If "5 players were added:\n[array of the names]"\n Was printed, then the code works.')    player.bet = 5
    print(f"Player {player.name}'s hand: {player.hand}, the bet: {player.bet}")
    player.doubledown()
    print(f"Player {player.name}'s hand: {player.hand}, the bet: {player.bet}")
    print("New hand should have an extra card, net bet should be double the bet.")
    
def inscheck():
    print("For test to work, hashtag out the round1 == True requirement.")
    player = Player("tester")
    players.append(player)
    dealer = Dealer(players)
    while True:
        which = input("Do you want Dealer to have Blackjack (y or n)?")
        if which in ("y","n"):
            break
        print("y or n please")
    player.bet = 50
    print("player bet is 50.")
    print("type y to actually test")
    if which == "y":
        dealer.dealerhand = ["h1","hk"]
        player.insurance(dealer)
        print(f'The phrase: "Dealer has Blackjack! Insurance bets are doubled and returned." should be printed.\nMoney total: {player.money} (should be 1525).')
    else:   
        dealer.dealerhand = ["h1","h9"]
        player.insurance(dealer)
        print(f'The phase: "Dealer does NOT have Blackjack, all insurance is lost." should be printed. \nMoney total: {player.money} (should be 1475).')
    
def test_deal1():
    # Set up test players
    numberOfPlayers = 3
    players = [Player('testplr' + str(i)) for i in range(numberofPlayers)]
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






