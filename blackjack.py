import random
from deck_of_cards import Deck
players = [] #players

def getting_players(): #ask players for player amount and names
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
        self.hasddown = False
    
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

    def getbet(self):  #get the amount players want to bet
        while True:
            try:
                bet = int(input(f"How much money would {self.name} like to bet? Betting is limited from $2-$500."))
                if bet >= 2 and bet <= self.money and bet <= 500:
                    self.money -= bet
                    self.bet = bet
                    print(f"{self.name} has bet {self.bet}!\nYou have ${self.money} left.")
                    return bet
                else:
                    print(f"Invalid amount (must be between 2 and 500).\nCurrent amount: {self.money}")
            except ValueError:
                print("Use a number.")

    def playerround(self, dealer):
        if self.hasddown:
            print(f"{self.name} has doubled down, they are unable to take an action.")
            return
        while True:
            hitstand = input("Would you like to hit or stand (h or s)?").strip().lower()
            if hitstand == "h":
                self.newcard(1)
                currenttot = self.handtotal()
                print(f"{self.name} has hit! Their card: \033[1m{deck.identify_card(self.hand[-1])}\033[0m.\nTheir total: {currenttot}.")
                if currenttot >= 21:
                    break
            elif hitstand == "s":
                break
            else:
                print('use "h" or "s" please')
                    
    def splitting(self, dealer=None):
        if len(self.hand) == 2 and self.hand[0][1] == self.hand[1][1]:
            if not self.hasddown:
                while True:
                    ifsplit = input(f"Would {self.name} like to split their hand? (y or n)? ").strip().lower()
                    if ifsplit in ("y", "n"):
                        break
                    print("y or n please")
                if ifsplit == "y":
                    if self.money >= self.bet:
                        splitcard = self.hand.pop() 
                        self.newcard(1)  
                        splitplayer = Player(f"{self.name} Split", self.money)
                        splitplayer.hand = [splitcard]
                        splitplayer.bet = self.bet
                        self.money -= self.bet
                        splitplayer.newcard(1)
                        players.append(splitplayer)
                        print(f"{self.name} has 2 hands.")
                    else:
                        print(f"You don't have enough money to make a split! Currently, you have {self.money}.")
            else:
                print(f"{self.name} has doubled down, they are unable to split.")

    def doubledown(self):
        currenttot = self.handtotal()
        if currenttot == 9 or currenttot == 10 or currenttot == 11:
            while True:
                ifdouble = input(f"Would {self.name} like to double down? (y or n)?\nNote that you can no longer hit or stand if you do.").strip().lower()
                if ifdouble in ("y", "n"):
                    break
                print("y or n please")
            if ifdouble == "y":
                if self.money >= self.bet:
                    self.newcard(1)
                    self.money -= self.bet
                    self.bet = self.bet * 2
                    print(f"{self.name} has doubled down! They get one card and cannot play anymore.")
                    self.hasddown = True
                    return True
                else:
                    print(f"You don't have enough money to double your bet! Currently, you have {self.money}.")
                    return False
        return False

    def insurance(self, dealer):
        if card_value(dealer.dealerhand[0]) == 11:
            while True:
                ifins = input(f"Would {self.name} like insurance (y or n)?\nNote that this version of insurance will automatically take half your original bet.").strip().lower()
                if ifins in ("y","n"):
                    break
                print("y or n please")
            if ifins == "y":
                if self.money >= 0.5 * self.bet:
                    self.insbet = 0.5 * self.bet
                    self.money -= 0.5 * self.bet
                    print(f"{self.name} has put ${self.insbet} in as insurance!")
                    if card_value(dealer.dealerhand[1]) == 10: 
                        print("Dealer has Blackjack! Insurance bets are doubled and returned.")
                        self.money += self.insbet * 2
                        self.insbet = 0
                    else:
                        print("Dealer does NOT have Blackjack, all insurance is lost.")
                        self.insbet = 0
            else:
                print(f"{self.name} does not have enough money!")
                    
class Bot(Player):
    def __init__(self,name,personality, money=1500):
        super().__init__(name,money)
        self.personality = personality #1 = aggro, 2 = neutral, 3 = safe, 4 = wildcard
        self.money = money
        
    def getbet(self):  #get the amount players want to bet
        if self.personality == 1:
            mini = 350
            maxi = 500
            botbet = min(random.randint(mini, maxi), self.money)
            if self.money < mini:
                if random.random() < 0.5:
                    botbet = self.money
                else:
                    zero = max(0, self.money - 150)
                    botbet = random.randint(zero, self.money)
            self.bet = botbet
            self.money -= botbet
            print(f"{self.name} has bet {self.bet}!\nThey have ${self.money} left.")
        elif self.personality == 2:
            mini = 150
            maxi = 375
            botbet = min(random.randint(mini, maxi), self.money)
            if self.money < mini:
                if random.random() < 0.5:
                    botbet = self.money
                else:
                    zero = max(0, self.money - 150)
                    botbet = random.randint(zero, self.money)
            self.bet = botbet
            self.money -= botbet
            print(f"{self.name} has bet {self.bet}!\nThey have ${self.money} left.")
        elif self.personality == 3:
            mini = 2
            maxi = 150
            botbet = min(random.randint(mini, maxi), self.money)
            if self.money < mini:
                if random.random() < 0.5:
                    botbet = self.money
                else:
                    zero = max(0, self.money - 150)
                    botbet = random.randint(zero, self.money)
            self.bet = botbet
            self.money -= botbet
            print(f"{self.name} has bet {self.bet}!\nThey have ${self.money} left.")
        elif self.personality == 4:
            mini = 2
            maxi = 500
            botbet = min(random.randint(mini, maxi), self.money)
            if self.money < mini:
                if random.random() < 0.5:
                    botbet = self.money
                else:
                    zero = max(0, self.money - 150)
                    botbet = random.randint(zero, self.money)
            self.bet = botbet
            self.money -= botbet
            print(f"{self.name} has bet {self.bet}!\nThey have ${self.money} left.")

    def playerround(self, dealer):
        p1rand = random.randint(17,19)
        p3rand = random.randint(15,17)
        p4rand = random.randint(1,20)
        if self.hasddown:
            print(f"{self.name} has doubled down, they are unable to take an action.")
            return
        while True:
            currenttot = self.handtotal()
            if self.personality == 1:
                if currenttot <= p1rand:
                    self.newcard(1)
                    ctot = self.handtotal()
                    print(f"{self.name} has hit! Their card: \033[1m{deck.identify_card(self.hand[-1])}\033[0m.\nTheir total: {ctot}.")
                    if ctot >= 21:
                        break
                else:
                    ctot = self.handtotal()
                    print(f"{self.name} stands!\nTheir total: {ctot}")
                    break
            elif self.personality == 2:
                if currenttot <= 17:
                    self.newcard(1)
                    ctot = self.handtotal()
                    print(f"{self.name} has hit! Their card: \033[1m{deck.identify_card(self.hand[-1])}\033[0m.\nTheir total: {ctot}.")
                    if ctot >= 21:
                        break
                else:
                    ctot = self.handtotal()
                    print(f"{self.name} stands!\nTheir total: {ctot}")
                    break
            elif self.personality == 3:
                if currenttot <= p3rand:
                    self.newcard(1)
                    ctot = self.handtotal()
                    print(f"{self.name} has hit! Their card: \033[1m{deck.identify_card(self.hand[-1])}\033[0m.\nTheir total: {ctot}.")
                    if ctot >= 21:
                        break
                else:
                    ctot = self.handtotal()
                    print(f"{self.name} stands!\nTheir total: {ctot}")
                    break
            elif self.personality == 4:
                if currenttot <= p4rand:
                    self.newcard(1)
                    ctot = self.handtotal()
                    print(f"{self.name} has hit! Their card: \033[1m{deck.identify_card(self.hand[-1])}\033[0m.\nTheir total: {ctot}.")
                    if ctot >= 21:
                        break
                else:
                    ctot = self.handtotal()
                    print(f"{self.name} stands!\nTheir total: {ctot}")
                    break
    
    def splitting(self, dealer):
        if len(self.hand) == 2 and self.hand[0][1] == self.hand[1][1]:
            if not self.hasddown:
                if self.personality == 1:
                    if self.money >= self.bet:
                        splitcard = self.hand.pop() 
                        self.newcard(1)  
                        splitplayer = Bot(f"{self.name} Split",self.personality,self.money)
                        splitplayer.hand = [splitcard]
                        splitplayer.bet = self.bet
                        self.money -= self.bet
                        splitplayer.newcard(1)
                        players.append(splitplayer)
                        print(f"{self.name} has 2 hands.")
                    else:
                        print(f"{self.name} doesn't have enough money to make a split! Currently, they have {self.money}.")
                elif self.personality == 2 and card_value(dealer.dealerhand[0]) <= 6:
                    if self.money >= self.bet:
                        splitcard = self.hand.pop() 
                        self.newcard(1)  
                        splitplayer = Bot(f"{self.name} Split",self.personality,self.money)
                        splitplayer.hand = [splitcard]
                        splitplayer.bet = self.bet
                        self.money -= self.bet
                        splitplayer.newcard(1)
                        players.append(splitplayer)
                        print(f"{self.name} has 2 hands.")
                    else:
                        print(f"{self.name} doesn't have enough money to make a split! Currently, they have {self.money}.")
                elif self.personality == 4:
                    r = random.randint(1,2)
                    if r == 1:
                        if self.money >= self.bet:
                            splitcard = self.hand.pop() 
                            self.newcard(1)  
                            splitplayer = Bot(f"{self.name} Split",self.personality,self.money)
                            splitplayer.hand = [splitcard]
                            splitplayer.bet = self.bet
                            self.money -= self.bet
                            splitplayer.newcard(1)
                            players.append(splitplayer)
                            print(f"{self.name} has 2 hands.")
                        else:
                            print(f"{self.name} doesn't have enough money to make a split! Currently, they have {self.money}.")
            else:
                print(f"{self.name} has doubled down, they are unable to split.")

    def doubledown(self):
        currenttot = self.handtotal()
        if currenttot == 9 or currenttot == 10 or currenttot == 11:
            if self.personality == 1:
                if self.money >= self.bet:
                    self.newcard(1)
                    self.money -= self.bet
                    self.bet = self.bet * 2
                    print(f"{self.name} has doubled down! They get one card and cannot play anymore.")
                    self.hasddown = True
                    return True
                else:
                    print(f"You don't have enough money to double your bet! Currently, you have {self.money}.")
                    return False   
            elif self.personality == 4:
                r = random.randint(1,2)
                if r == 1:
                    if self.money >= self.bet:
                        self.newcard(1)
                        self.money -= self.bet
                        self.bet = self.bet * 2
                        print(f"{self.name} has doubled down! They get one card and cannot play anymore.")
                        self.hasddown = True
                        return True
                    else:
                        print(f"You don't have enough money to double your bet! Currently, you have {self.money}.")
                        return False   
                
        return False

    def insurance(self, dealer):
        if card_value(dealer.dealerhand[0]) == 11:
            if self.personality == 1:
                if self.money >= 0.5 * self.bet:
                    self.insbet = 0.5 * self.bet
                    self.money -= 0.5 * self.bet
                    print(f"{self.name} has put ${self.insbet} in as insurance!")
                    if card_value(dealer.dealerhand[1]) == 10: 
                        print("Dealer has Blackjack! Insurance bets are doubled and returned.")
                        self.money += self.insbet * 2
                        self.insbet = 0
                    else:
                        print("Dealer does NOT have Blackjack, all insurance is lost.")
                        self.insbet = 0
                else:
                    print(f"{self.name} does not have enough money!")
            if self.personality ==  4:
                r = random.randint(1,2)
                if r == 1:
                    if self.money >= 0.5 * self.bet:
                        self.insbet = 0.5 * self.bet
                        self.money -= 0.5 * self.bet
                        print(f"{self.name} has put ${self.insbet} in as insurance!")
                        if card_value(dealer.dealerhand[1]) == 10: 
                            print("Dealer has Blackjack! Insurance bets are doubled and returned.")
                            self.money += self.insbet * 2
                            self.insbet = 0
                        else:
                            print("Dealer does NOT have Blackjack, all insurance is lost.")
                            self.insbet = 0
                    else:
                        print(f"{self.name} does not have enough money!")
                    
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
        self.dealerhand = deck.deal(2)
        self.dealershow()
        for player in self.players:
            player.insurance(self)
            player.doubledown()
            player.splitting(self)

    def playerbets(self): #uses getbet
        for player in self.players:
            player.getbet()
    
    def dealershow(self): #dealer shows one card
        print(f"The Dealer reveals a card: {deck.identify_card(self.dealerhand[0])}.")
    
    def round(self): #player: hit or stand, if over 21, bust
        pass

    def dealerturn(self): #dealer play, if under 17, will play, if not, will stand
        while self.dealer_value() < 17:
            new_cards = deck.deal(1)
            self.dealerhand += new_cards
            print(f"Dealer hits: \033[1m{deck.identify_card(new_cards[0])}\033[0m, hand now: {self.dealer_value()}")
        print(f"Dealer stands with {self.dealer_value()}")

    def dealer_value(self): #dealer total value, will handle aces
        value = 0
        aces = False
        for card in self.dealerhand:
            if card_value(card) == 11:
                aces = True
                value += 1
            else:
                value += card_value(card)
        if aces == True and value <= 11:
            value += 10
        return value

    def check(self): #see if anyone busts or wins or ties
        pass

#Tests: -------------------------------------------------------------------------------------
 player_init_test

    def test_player_init():
        p1 = Player("Jason", 50)

        print(p1.name)
        print(p1.money)

        if p1.name = "Jason"
            print("test passed")
        else:
            print("test failed")

        if p1.money = "2000"
            print("test passed")
        else:
            print("test failed")


def test_getting_players():
    x = random.randint(2,10)
    print(f"Your job: attempt {x} players.")
    getting_players()
    print(f'If "{x} players were added:\n[array of the names]"\nWas printed, then the code works.')
    players.clear()
    
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
    players.clear()

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
    players.clear()

def splitcheck():
    print("type y to actually test")
    player = Player("tester")
    players.append(player)
    dealer = Dealer(players)
    player.hand = ["h2", "d2"]
    print(f"Current hand: {player.hand}.")
    player.splitting()
    print('If "tester has 2 hands." is printed, it should be good. \nPrinting hands now.')
    for player in players:
        print(f"Player {player.name}: {player.hand}")
    print("Ideally, both players should have one card of the same rank, and another random card.") 
    players.clear()

def doubledowncheck():
    print("type y to actually test")
    player = Player("tester")
    players.append(player)
    dealer = Dealer(players)
    player.hand = ["h5","h6"]
    player.bet = 50
    print(f"Player {player.name}'s hand: {player.hand}, the bet: {player.bet}")
    player.doubledown()
    print(f"Player {player.name}'s new hand: {player.hand}, the bet: {player.bet}")
    print("New hand should have an extra card, net bet should be double the bet.")
    players.clear()
    
def inscheck():
    player = Player("tester")
    players.append(player)
    dealer = Dealer(players)
    while True:
        which = input("Do you want Dealer to have Blackjack (y or n)?").strip().lower()
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
    players.clear()
    
def test_deal1():
    # Set up test players
    numberOfPlayers = 3
    players = [Player('testplr' + str(i)) for i in range(numberOfPlayers)]
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
    players.clear()




