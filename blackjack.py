import random #for shuffling
from deck_of_cards import Deck
players = [] #players

class Card: #card properties
    def __init__(self,suit,rank,value): #creating card
        self.suit = suit #suit
        self.rank = rank #rank
        self.value = value #value

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
    
class Dealer: #dealer properties
    def __init__(self, players): #creating dealer + what its actions will be
        self.deck = Deck() #taking deck
        self.players = players #taking players
        self.dealerhand = [] #dealer's hand of cards
        self.pot = 0 #money in the pot

    def deal1(self): #first deal for all players

    def dealershow(self): #dealer shows one card
    
    def round(self): #player: hit or stand, if over 21, bust

    def dealerturn(self): #dealer play, if under 17, will play, if not, will stand

    def dealer_value(self): #dealer total value, will handle aces

    def check(self): #see if anyone busts or wins or ties



