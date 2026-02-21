import random
import time
import pickle
from deck_of_cards import Deck
players = [] #players

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
        self.personality = 0
        self.insbet = 0
    
    def newcard(self, count): #putting card in hand
        self.hand += deck.deal(count)
        
    def resethand(self): #reset hand
        self.hand = []

    def reset_player(self):
        self.hand = []
        self.bet = 0
        self.hasddown = False
    
    def player_value(self): #total value of cards + will handle ace shenanigans
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
        print(f"{self.name} has ${self.money}.")
        while True:
            try:
                bet = int(input(f"How much money would {self.name} like to bet? Betting is limited from $2-$500.\n"))
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
        print(f"{self.name}'s cards:")
        for card in self.hand:
            print(f"\033[1m{deck.identify_card(card)}\033[0m.")
        print(f"Total: {self.player_value()}.")
        while True:
            hitstand = input(f"{self.name}, would you like to hit or stand (h or s)?\n").strip().lower()
            if hitstand == "h":
                self.newcard(1)
                currenttot = self.player_value()
                print(f"{self.name} has hit! Their card: \033[1m{deck.identify_card(self.hand[-1])}\033[0m.\nTheir total: \033[1m{currenttot}\033[0m.")
                if currenttot >= 21:
                    break
            elif hitstand == "s":
                print(f"{self.name} stands! Their total: \033[1m{self.player_value()}\033[0m.")
                break
            else:
                print('use "h" or "s" please')
                    
    def splitting(self, dealer=None):
        if len(self.hand) == 2 and self.hand[0][1] == self.hand[1][1]:
            if not self.hasddown:
                while True:
                    ifsplit = input(f"Would {self.name} like to split their hand? (y or n)?\n").strip().lower()
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
                        print(f"{self.name}'s new hand: \033[1m{deck.identify_card(self.hand[0])}, {deck.identify_card(self.hand[1])}\033[0m.")
                        print(f"{players[-1].name}'s new hand:\033[1m{deck.identify_card(players[-1].hand[0])}, {deck.identify_card(players[-1].hand[1])}\033[0m.")
                    else:
                        print(f"You don't have enough money to make a split! Currently, you have {self.money}.")
            else:
                print(f"{self.name} has doubled down, they are unable to split.")

    def doubledown(self):
        currenttot = self.player_value()
        if currenttot == 9 or currenttot == 10 or currenttot == 11:
            while True:
                ifdouble = input(f"Would {self.name} like to double down? (y or n)?\nNote that you can no longer hit or stand if you do.\n").strip().lower()
                if ifdouble in ("y", "n"):
                    break
                print("y or n please")
            if ifdouble == "y":
                if self.money >= self.bet:
                    self.newcard(1)
                    self.money -= self.bet
                    self.bet = self.bet * 2
                    print(f"{self.name} has doubled down! They get one card and must stand.")
                    self.hasddown = True
                    return True
                else:
                    print(f"You don't have enough money to double your bet! Currently, you have {self.money}.")
                    return False
        return False
                    
class Bot(Player):
    def __init__(self,name,personality, money=1500):
        super().__init__(name,money)
        self.personality = personality #1 = aggro, 2 = neutral, 3 = safe, 4 = wildcard
        self.money = money
        
    def getbet(self):  #get the amount players want to bet
        personality_bets = {
            1: {"mini": 350, "maxi": 500, "randchance": 0.5, "randbet": 150},
            2: {"mini": 150, "maxi": 375, "randchance": 0.25, "randbet": 75},
            3: {"mini": 2, "maxi": 150, "randchance": 0.05, "randbet": 75},
            4: {"mini": 2, "maxi": 500, "randchance": 0.75, "randbet": 150},
            5: {"mini": 500, "maxi": 500, "randchance": 1, "randbet":150}
        }
        pbet = personality_bets[self.personality]
        mini, maxi, randchance, randbet = pbet["mini"], pbet["maxi"], pbet["randchance"], pbet["randbet"]
        botbet = min(random.randint(mini, maxi), self.money)
        if self.money < mini:
            if random.random() < randchance:
                botbet = self.money
            else:
                zero = max(0, self.money - randbet)
                botbet = random.randint(zero, self.money)
        self.bet = botbet
        self.money -= botbet
        print(f"{self.name} has bet ${self.bet}!\nThey have ${self.money} left.")

    def playerround(self, dealer):
        if self.hasddown:
            print(f"{self.name} has doubled down, they are unable to take an action.")
            return
        bot_randomnum = {
            1: lambda: random.randint(17,19),
            2: lambda: 17,
            3: lambda: random.randint(15,17),
            4: lambda: random.randint(1,20),
            5: lambda: 17
        }
        b_rand = bot_randomnum[self.personality]()
        while True:
            currenttot = self.player_value()
            if currenttot <= b_rand:
                self.newcard(1)
                ctot = self.player_value()
                print(f"{self.name} has hit! Their card: \033[1m{deck.identify_card(self.hand[-1])}\033[0m.\nTheir total: \033[1m{ctot}\033[0m.")
                if ctot >= 21:
                    break
            else:
                ctot = self.player_value()
                print(f"{self.name} stands!\nTheir total: \033[1m{ctot}\033[0m")
                break
    
    def splitting(self, dealer):
        if len(self.hand) == 2 and self.hand[0][1] == self.hand[1][1]:
            if not self.hasddown:
                if (self.personality == 1) or \
                    (self.personality == 2 and card_value(dealer.dealerhand[0]) <= 6) or \
                    (self.personality == 4 and random.randint(1,2) == 1):
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
                        print(f"{self.name}'s new hand: \033[1m{deck.identify_card(self.hand[0])}, {deck.identify_card(self.hand[1])}\033[0m.")
                        print(f"{players[-1].name}'s new hand:\033[1m{deck.identify_card(players[-1].hand[0])}, {deck.identify_card(players[-1].hand[1])}\033[0m.")
                    else:
                        print(f"{self.name} doesn't have enough money to make a split! Currently, they have {self.money}.")
            else:
                print(f"{self.name} has doubled down, they are unable to split.")

    def doubledown(self):
        currenttot = self.player_value()
        if currenttot == 9 or currenttot == 10 or currenttot == 11:
            if (self.personality == 1) or \
                (self.personality == 4 and random.randint(1,2) == 1):
                if self.money >= self.bet:
                    self.newcard(1)
                    self.money -= self.bet
                    self.bet = self.bet * 2
                    print(f"{self.name} has doubled down! They get one card and must stand.")
                    self.hasddown = True
                    return True
                else:
                    print(f"You don't have enough money to double your bet! Currently, you have {self.money}.")
                    return False   
            return False
        return False
                    
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
            self.insurance()
            player.doubledown()
            player.splitting(self)

    def playerbets(self): #uses getbet
        for player in self.players:
            player.getbet()
    
    def dealershow(self): #dealer shows one card
        print(f"The Dealer reveals a card: \033[1m{deck.identify_card(self.dealerhand[0])}\033[0m.")
    
    def round(self): #player: hit or stand, if over 21, bust
        for player in players:
            player.playerround(self)
        print(f"The Dealer's hole card: \033[1m{deck.identify_card(self.dealerhand[1])}\033[0m")
        self.dealerturn()
        self.check()

    def dealerturn(self): #dealer play, if under 17, will play, if not, will stand
        while self.dealer_value() < 17:
            new_cards = deck.deal(1)
            self.dealerhand += new_cards
            print(f"Dealer hits: \033[1m{deck.identify_card(new_cards[0])}\033[0m, hand now: \033[1m{self.dealer_value()}\033[0m.")
        print(f"Dealer stands with \033[1m{self.dealer_value()}\033[0m")

    def dealer_value(self): #dealer total value, will handle aces
        total = 0
        for card in self.dealerhand:
            total += card_value(card)
        if total > 21: # Lowers the value of aces to 1 if the total is over 21
            for card in self.dealerhand:
                if card_value(card) == 11:
                    total -= 10 #Should just redo total every time it checks... inefficient, but will work
                    if total <= 21:
                        break
        return total

    def insurance(self):
        if card_value(self.dealerhand[0]) == 11:
            for player in self.players:
                if (player.personality == 1) or \
                (player.personality == 4 and random.randint(1,2) == 1):
                    ifins = "y"
                else:
                    while True:
                        ifins = input(f"Would {player.name} like insurance (y or n)?\nNote that this version of insurance will automatically take half your original bet.\n").strip().lower()
                        if ifins in ("y","n"):
                            break
                        print("y or n please")
                if ifins == "y":
                    if player.money >= 0.5 * player.bet:
                        player.insbet = 0.5 * player.bet
                        player.money -= 0.5 * player.bet
                        print(f"{player.name} has put ${player.insbet} in as insurance!")
                    else:
                        print(f"{player.name} does not have enough money!")
                if card_value(self.dealerhand[1]) == 10: 
                    print("Dealer has Blackjack! Insurance bets are doubled and returned.")
                    player.money += player.insbet * 2
                    player.insbet = 0
                else:
                    print("Dealer does NOT have Blackjack, all insurance is lost.")
                    player.insbet = 0
        
    
    def check(self): #see if anyone busts or wins or ties
        dealer = self.dealer_value()
        for player in players:
            if player.hasddown == True:
                print(f"{player.name} had doubled down, and their final card is...\n\033[1m{deck.identify_card(player.hand[-1])}\033[0m!")
            checks = player.player_value()
            if checks > 21:
                print(f"{player.name} busts! You lose. Lost: ${player.bet}.\n Dealer value:\033[1m{dealer}\033[0m, {player.name} value:\033[1m{checks}\033[0m.")
            elif dealer > 21:
                print(f"Dealer busts! {player.name} wins: ${player.bet * 2}.\n Dealer value:\033[1m{dealer}\033[0m, {player.name} value:\033[1m{checks}\033[0m.")
                player.money += player.bet * 2
            elif (checks == 21 and len(player.hand) == 2) and (dealer != 21 or len(self.dealerhand) > 2):
                print(f"{player.name} has BlackJack! Won: ${player.bet * 1.5}.\n Dealer value:\033[1m{dealer}\033[0m, {player.name} value:\033[1m{checks}\033[0m.")
                player.money += player.bet * 1.5
            elif checks > dealer:
                print(f"{player.name} wins! Won: ${player.bet * 2}.\n Dealer value:\033[1m{dealer}\033[0m, {player.name} value:\033[1m{checks}\033[0m.")
                player.money += player.bet * 2
            elif (dealer == 21 and len(self.dealerhand) == 2) and (checks != 21 or len(player.hand) >2):
                print(f"Dealer has BlackJack! {player.name} loses. Lost {player.bet}.\n Dealer value:, {player.name} value:\033[1m{checks}\033[0m.")
            elif checks < dealer:
                print(f"Dealer wins! {player.name} loses. Lost: ${player.bet}.\n Dealer value:\033[1m{dealer}\033[0m, {player.name} value:\033[1m{checks}\033[0m.")
            elif checks == dealer: #maybe add condition if double BlackJack, just to say they both had it, but doesn't really matter.
                print(f"{player.name} ties with the Dealer. No loss/gain.\n Dealer value:\033[1m{dealer}\033[0m, {player.name} value:\033[1m{checks}\033[0m.")
                player.money += player.bet
            player.bet = 0
            player.hasddown = False

#Game playing: -----------------------------------------------------------------------------------------------
def randbotp():
    personality = [1,2,3,4,5]
    percentchance = [20,40,20,10,10]
    return random.choices(personality, weights=percentchance)[0]

def getting_players(): #ask players for player/bot amount and names
    while True:
        try:
            pnum = int(input("How many players are you adding?"))
            break
        except ValueError:
            print("a number (don't use letters) please")
    for i in range(pnum):
        name = input(f"Player {i + 1}'s name: ")
        players.append(Player(name))
    while True:
        try:
            bnum = int(input("How many bots do you want?"))
            break
        except ValueError:
            print("a number (don't use letters) please")
    for j in range(bnum):
        players.append(Bot("Bot" + str(j), randbotp()))
    print(f"{pnum} players were added:\n{[pl.name for pl in players]} \n{bnum} bots were also added.\n")
    
def reset_game():
    global players
    while True:
        reset = input(f'''Would you like to continue this game (y = continue, n = reset)?
And with the same players (y or n)?
Type them together, e.g. "yy" or "yn". 1st is restart, 2nd is players.
Just type n if you do not want to restart:''').strip().lower()
        if reset in ("yy","yn","n"):
            break
        print('Please type a valid answer. Valid: "yy", "yn","n".')
    if reset == "n":
        while True:
            save = input("Would you like to save your game (y or n)?\nSaved: players, money, wins.") #wins implemented later prob
            if save in ("y","n"):
                break
            print("y or n please")
        if save == "y":
            while True:
                try:
                    whichsave = int(input("Save in 1, 2, or 3?")) #will show what's in saves later once I figure that out
                    if whichsave in (1,2,3):
                        break
                    else:
                        print("Use a valid number please.")
                except:
                    print("Use a number.")
            with open(f'load{whichsave}.pkl', 'wb') as f:
                pickle.dump(players, f)
        elif save == "n":   
            players.clear()
            quit()
    elif reset == "yy":
        for player in players:
            player.reset_player()
        run_game()
    elif reset == "yn":
        for player in players:
            player.reset_player()
        while True:
            try:
                for player in players:
                    print(player.name)
                remove_players = int(input(f"""Who would you like to remove?
Assume the 1st player (top) is numbered 1, the 2nd 2, etc.
If you are removing multiple players, type it with commas inbetween.
EX: 1,2,6,8""").strip())
                if remove_players > len(players) + 1 or new_players < 1:
                    print("Please enter a valid player.")
                else:
                    break
            except ValueError:
                print("Please enter an integer (whole number).")
        remove_players = remove_players.split(",")
        players = [plr for plr in players if plr not in remove_players]
        getting_players()
        run_game()
        
def run_game():
    dealer = Dealer(players)
    if players == []:
        getting_players()
    dealer.playerbets()
    dealer.deal1()
    dealer.round()
    input("Enter any key to continue: ")
    reset_game()

def menu():
    global players
    def delete_menu(num, slow=True):
        for i in range(num):
            print("\033[A\033[K", end='\r')
            if slow == True:
                time.sleep(0.025)

    def wrong_num():
        print("Use a correct number please.")
        time.sleep(2)
        delete_menu(2)

    def menu_nav():
        while True:
            try:
                menu_input = int(input().strip())
                if menu_input in (1,2,3,4):
                    break
                else:
                    wrong_num()
            except:
                wrong_num()
        return menu_input

    def main_menu():
        global players
        delete_menu(1000,False)
        for i in mainmenu:
            print(i)
            time.sleep(0.5)
        print("Use given numbers to navigate")
        menu_input = menu_nav()
        if menu_input == 1:
            players.clear()
            run_game()
        elif menu_input == 2:
            delete_menu(7)
            for i in loadmenu:
                print(i)
                time.sleep(0.5)
            load_input = menu_nav()
            if load_input == 1 or load_input == 2 or load_input == 3:
                with open(f'load{whichsave}.pkl', 'rb') as f:
                    players = pickle.load(f)
                print(f"Save {load_input} was loaded!")
                run_game()
            elif load_input == 4:
                main_menu()
        elif menu_input == 3:
            delete_menu(7)
            print("https://bicyclecards.com/how-to-play/blackjack")
            while True:
                exit = input("Type anything to go back to main menu")
                if exit != "":
                    break
            main_menu()
        elif menu_input == 4:
            delete_menu(7)
            quit()

    mainmenu = ["BLACKJACK", "New Game - 1", "Load Save - 2", "Rules - 3", "Exit - 4"]
    loadmenu = ["BLACKJACK SAVES","SAVE1 - 1", "SAVE2 - 2", "SAVE3 - 3", "Exit - 4"]

    main_menu()

menu()

#Tests: -------------------------------------------------------------------------------------
def test_player_init():
    p1 = Player("Jason", 50)

    print(p1.name)
    print(p1.money)

    if p1.name == "Jason":
        print("name test passed")
    else:
        print("name test failed")

    if p1.money == 50:
        print("money test passed")
    else:
        print("money test failed")


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
            result = plr.player_value()
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
        dealer.insurance()
        print(f'The phrase: "Dealer has Blackjack! Insurance bets are doubled and returned." should be printed.\nMoney total: {player.money} (should be 1525).')
    else:   
        dealer.dealerhand = ["h1","h9"]
        dealer.insurance()
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




