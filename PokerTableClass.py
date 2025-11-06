#Texas Hold Em Specific
from deck_of_cards import Deck
from collections import Counter
from itertools import combinations

class Player: #player properties
    def __init__(self,name,money=1500): #creating player, give money
        self.name = name #player name, may not use because they'll see each other's cards?
        self.hand = [] #hand of cards
        self.money = money #money amount
        self.bet #Money in pot

    def newcard(self, count): #putting card in hand
        self.hand += Deck.deal(count)
        
    def resethand(self): #reset hand
        self.hand = []

class poker_table:
    def __init__(self):
        self.players = [] #List of players, need a player class
        self.pot = 0
        self.bets = []
        self.deck = Deck(False,True,True)
        self.table_cards = []
        self.current_player = None
        self.button_player = None

    def deal_hands(self): #Gives each player their initial two pocket cards
        return None

    def deal_table(self): #Adds cards to the table as needed
        return None

    #Identifies the best hand which can be made with the set of cards
    def best_hand(self,cards):

        # rank mapping (0 = 10, 1 = Ace)
        rank_map = {'0':10, '1':14, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,
                    '9':9, 'j':11, 'q':12, 'k':13}
        
        best_score = -1
        
        # Check all 5-card combinations
        for combo in combinations(cards, 5):
            suits = [c[0] for c in combo]
            ranks = [c[1] for c in combo]
            values = sorted([rank_map[r] for r in ranks])
            
            # Handle Ace-low straight
            is_ace_low_straight = values == [2, 3, 4, 5, 14]
            if is_ace_low_straight:
                values = [1, 2, 3, 4, 5]
            
            counts = Counter(values)
            count_values = sorted(counts.values(), reverse=True)
            
            is_flush = len(set(suits)) == 1
            is_straight = all(values[i] - values[i-1] == 1 for i in range(1, 5))
            
            # Determine hand rank
            if is_flush and is_straight and max(values) == 14:
                rank = 9  # Royal Flush
            elif is_flush and is_straight:
                rank = 8  # Straight Flush
            elif count_values == [4, 1]:
                rank = 7  # Four of a Kind
            elif count_values == [3, 2]:
                rank = 6  # Full House
            elif is_flush:
                rank = 5  # Flush
            elif is_straight:
                rank = 4  # Straight
            elif count_values == [3, 1, 1]:
                rank = 3  # Three of a Kind
            elif count_values == [2, 2, 1]:
                rank = 2  # Two Pair
            elif count_values == [2, 1, 1, 1]:
                rank = 1  # One Pair
            else:
                rank = 0  # High Card
            
            # Sort values by (frequency, then rank)
            sorted_values = sorted(values, key=lambda x: (counts[x], x), reverse=True)
            tiebreaker = sum(v * (15**(4-i)) for i, v in enumerate(sorted_values))
            score = rank * (15**5) + tiebreaker
            
            if score > best_score:
                best_score = score
        
        return best_score
        

    def evaluate_hand(self, hand_str):
        # Parse hand: e.g. "AS KS QS JS TS" -> [('A','S'), ('K','S'), ...]
        cards = hand_str.split()
        ranks = [c[0] for c in cards]
        suits = [c[1] for c in cards]
        
        # Map ranks to values
        rank_map = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,
                    '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
        values = sorted([rank_map[r] for r in ranks])
        
        # Check for Ace-low straight (A,2,3,4,5)
        is_ace_low_straight = values == [2, 3, 4, 5, 14]
        if is_ace_low_straight:
            values = [1, 2, 3, 4, 5]
        
        # Count occurrences of each rank
        counts = Counter(values)
        count_values = sorted(counts.values(), reverse=True)
        unique_values = sorted(counts.keys(), reverse=True)
        
        # Determine hand type
        is_flush = len(set(suits)) == 1
        is_straight = all(values[i] - values[i-1] == 1 for i in range(1,5))
        
        if is_flush and is_straight and max(values) == 14:
            rank = 9  # Royal Flush
        elif is_flush and is_straight:
            rank = 8  # Straight Flush
        elif count_values == [4, 1]:
            rank = 7  # Four of a Kind
        elif count_values == [3, 2]:
            rank = 6  # Full House
        elif is_flush:
            rank = 5  # Flush
        elif is_straight:
            rank = 4  # Straight
        elif count_values == [3, 1, 1]:
            rank = 3  # Three of a Kind
        elif count_values == [2, 2, 1]:
            rank = 2  # Two Pair
        elif count_values == [2, 1, 1, 1]:
            rank = 1  # One Pair
        else:
            rank = 0  # High Card
        
        # Return numeric score that reflects both type and tiebreakers
        # Example: (rank, sorted card values by frequency then rank)
        sorted_values = sorted(values, key=lambda x: (counts[x], x), reverse=True)
        tiebreaker = sum(v * (15**(i)) for i, v in enumerate(sorted_values))
        score = rank * (15**5) + tiebreaker
        return score


    def add_player(self): #adds a new player at the table
        return None

    def remove_player(self,player): #removes a player
        self.players.remove(player)

    def deal_round(self): #Goes through the steps of a poker round
        #gets blinds
        #deals pocket hands
        #calls for bets
        #deals to table and calls for bets (x3)
        #determines winning player or players
        #distributes winnings
        #moves button
        return None

    #Asks the player what they want to bet
    def player_bet(self,player,game_state):
        bet = 0
        return bet #A number for the size of the bet

#Tests ---------------------------------------------
def test_remove_player():
    table = poker_table()
    player1 = Player("Sophia")
    player2 = Player("Alvin")

    table.players = [player1, player2]

    table.remove_player(player2)

    assert player2 not in table.players
    assert player1 in table.players
    assert len(table.players) == 1

def test_best_hand():
    table = poker_table()
    hands = [
        ['c8',"c4","h3","h7","c2","c0","hj"], #Jack high
        ['c9',"c2","h1","s4","s6",'d9',"dk"], #pair of 9s
        ['c0',"h3","s4","c7","h8",'c6',"s2"], #10 high
        ['c6','c2','c9','h3','s4','d7','s8'], #9 high
        ['d3','c3','h3','s4','s6','dk','sq'], #Three of 3s
        ['d3','c3','h4','h8','s0','d1','s9'], #pair of 3s
        ['cj','d3','dj','s1','d6','hq','s2'], #pair of jacks
        ['ck','d5','h2','h4','d0','sq','d8'], #king high
        ['c7','d7','h7','s7','s2','sk','s6'], #four of a kind, 7s, jack kicker
        ['c7','d7','h7','ck','hq','d2','h5'], #three 7s
        ['c7','d7','h7','s7','s2','s1','s6'], #four of a kind, 7s, ace kicker
        ['c5','c1','c0','ck','d5','c2','h5'], #King high flush
        ['c6','d7','h2','h8','h9','ck','s0'], #10 high straight
        ['c2','c3','c4','d9','c5','c6','h2'], #6-high straight flush
        ['c1','c2','c3','c4','c5','d0','s8'], #5-high straight flush
        ['s1','sk','sq','s0','h8','sj','c6'], #Royal flush
        ['d3','c3','h3','s4','s6','dq','sq'] # 3s full of queens
    ]
    
        
    print(f"Identifies high card v1: {table.best_hand(hands[0]) > table.best_hand(hands[2])}")
    print(f"Identifies high card v2: {table.best_hand(hands[0]) > table.best_hand(hands[3])}")
    print(f"Identifies high card v2: {table.best_hand(hands[2]) > table.best_hand(hands[3])}")
    print(f"Identifies high card v3: {table.best_hand(hands[0]) < table.best_hand(hands[7])}")
    print(f"Identifies pair beats high card v1: {table.best_hand(hands[1]) > table.best_hand(hands[2])}")
    print(f"Identifies pair beats high card v2: {table.best_hand(hands[1]) > table.best_hand(hands[3])}")
    print(f"Identifies pair beats high card v3: {table.best_hand(hands[1]) > table.best_hand(hands[7])}")
    print(f"Identifies pair beats high card v4: {table.best_hand(hands[5]) > table.best_hand(hands[2])}")
    print(f"Identifies pair beats high card v5: {table.best_hand(hands[5]) > table.best_hand(hands[3])}")
    print(f"Identifies pair beats high card v6: {table.best_hand(hands[6]) > table.best_hand(hands[7])}")
    print(f"Identifies better pair: {table.best_hand(hands[1]) > table.best_hand(hands[5])}")
    print(f"Identifies three of a kind beats pair: {table.best_hand(hands[4]) > table.best_hand(hands[6])}")
    print(f"Identifies better three of a kind: {table.best_hand(hands[4]) < table.best_hand(hands[9])}")
    print(f"Identifies four of a kind beats three of a kind: {table.best_hand(hands[8]) > table.best_hand(hands[9])}")
    print(f"Identifies kickers: {table.best_hand(hands[10]) > table.best_hand(hands[8])}")
    print(f"Identifies flush beats straight: {table.best_hand(hands[12]) < table.best_hand(hands[11])}")
    print(f"Identifies full house beats flush: {table.best_hand(hands[11]) < table.best_hand(hands[16])}")
    print(f"Identifies four of a kind beats full house: {table.best_hand(hands[10]) > table.best_hand(hands[-1])}")
    print(f"Identifies straight flush beats flush: {table.best_hand(hands[11]) < table.best_hand(hands[-3])}")
    print(f"Identifies straight flush beats four of a kind: {table.best_hand(hands[10]) < table.best_hand(hands[-3])}")
    print(f"Identifies 6-high straight beats Ace-high straight: {table.best_hand(hands[-3]) < table.best_hand(hands[-4])}")
    print(f"Identifies royal flush beats generic straight flush: {table.best_hand(hands[-4]) < table.best_hand(hands[-2])}")
    
    def test_deal_hands():
        table = poker_table()
        table.players = [Player("Angela"), Player("Bob"), Player("Jeff")]
    
        table.deal_hands()
    
        for player in table.players:
            assert len(player.hand) == 2, f"{player.name} should have 2 cards"
       
        all_cards = []
        for player in table.players:
            for card in player.hand:
                all_cards.append(card)
        
        if len(all_cards) != len(set(all_cards)):
            print("There are duplicate cards.")
        else:
            print("It worked!!!")









