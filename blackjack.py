import random #for shuffling
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

    
class Dealer: #dealer properties
    def __init__(self, players): #creating dealer + what its actions will be
        self.deck = Deck() #taking deck
        self.players = players #taking players
        self.dealerhand = [] #dealer's hand of cards
        self.pot = 0 #money in the pot

    def deal1(self): #first deal for all players
        for player in self.players:
            player.newcard(2)
        self.dealerhand = deck.deal(2)
        #print(player.hand) will print for tests 
        #idk how we can reveal the player's cards without revealing it to the other players. Maybe discuss later?

    def dealershow(self): #dealer shows one card
        print(f"The Dealer reveals a card: {self.dealerhand[0]}.")
    
    def round(self): #player: hit or stand, if over 21, bust
        pass

    def dealerturn(self): #dealer play, if under 17, will play, if not, will stand
        pass

    def dealer_value(self): #dealer total value, will handle aces
        pass

    def check(self): #see if anyone busts or wins or ties
        dealer_total = 0
        # calculate dealer total safely
        try:
            dealer_total = 0
            for card in self.dealerhand:
                dealer_total += card_value(card)
            # handle Aces for dealer
            if dealer_total > 21:
                for card in self.dealerhand:
                    if card_value(card) == 11:
                        dealer_total -= 10
                        if dealer_total <= 21:
                            break
        except Exception as e:
            print(f"Error calculating dealer total: {e}")
            return

        print(f"\nDealer's final hand: {self.dealerhand} (Total: {dealer_total})")

        for player in self.players:
            player_total = player.handtotal()

            print(f"\n{player.name}'s hand: {player.hand} (Total: {player_total})")

            # --- BLACKJACK CHECKS ---
            if player_total == 21 and len(player.hand) == 2 and dealer_total != 21:
                print(f"{player.name} has Blackjack! They win 1.5x their bet.")
                player.money += int(player.bet * 1.5)
            elif dealer_total == 21 and len(self.dealerhand) == 2 and player_total != 21:
                print(f"Dealer has Blackjack! {player.name} loses their bet.")
                player.money -= player.bet

            # --- BUST CHECKS ---
            elif player_total > 21:
                print(f"{player.name} busts with {player_total}! Loses bet of {player.bet}.")
                player.money -= player.bet
            elif dealer_total > 21:
                print(f"Dealer busts! {player.name} wins {player.bet}.")
                player.money += player.bet

            # --- TOTAL COMPARISON ---
            else:
                if player_total > dealer_total:
                    print(f"{player.name} wins! Gains {player.bet}.")
                    player.money += player.bet
                elif player_total < dealer_total:
                    print(f"{player.name} loses. Dealer wins.")
                    player.money -= player.bet
                else:
                    print(f"{player.name} ties with the dealer. Bet returned.")

        print("\n--- ROUND COMPLETE ---")
        for player in self.players:
            print(f"{player.name} now has ${player.money}.")

#Tests: -------------------------------------------------------------------------------------
def resethand_checker():
    testclass = Player("L Bozo Code")
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

