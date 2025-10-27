#Texas Hold Em Specific

class poker_table:

    hand_values = {} #A dictionary identifying the name of numerically ordered hands

    def __init__(self):
        self.players = [] #List of players, need a player class
        self.pot = 0
        self.bets = []
        self.deck = None #Need a deck class
        self.table_cards = []
        self.current_player = None
        self.button_player = None

    def deal_hands(self): #Gives each player their initial two pocket cards
        return None

    def deal_table(self): #Adds cards to the table as needed
        return None

    #Identifies the best hand which can be made with the set of cards
    def best_hand(self,cards):
        hand_value = 0
        return hand_value #A number identifying the strength of the hand

    from collections import Counter

    def evaluate_hand(hand_str):
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
        tiebreaker = sum(v * (15**i) for i, v in enumerate(sorted_values))
        score = rank * (15**5) + tiebreaker
        return score


    def add_player(self): #adds a new player at the table
        return None

    def remove_player(self): #removes a player
        return None

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
def test_best_hand():
    table = poker_table()
    hands = [
        ['c8'], #8 high
        ['c9','d9'], #pair of 9s
        ['c9','c6'], #9 high
        ['c6','c2'], #6 high
        ['d3','c3','h3'], #Three of 3s
        ['d3','c3','h4'], #pair of 3s
        ['cj','d3','dj'], #pair of jacks
        ['ck','d5','h2'], #king high
        ['c7','d7','h7','s7'], #four of a kind, 7s
        ['c7','d7','h7','ck']] #three 7s
    print(f"Identifies high card v1: {table.best_hand(hands[0]) < table.best_hand(hands[2])}")
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


