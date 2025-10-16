# When dealing with codes on:
# c=clubs, h=hearts, d=diamonds, s=spades 
# j=jack, q=queen, k=king 
# 0s are 10s, 1s are aces

import random

class Deck:
    suits = {"c": "Clubs", "h": "Hearts", "d": "Diamonds", "s": "Spades"}

    def __init__(self, jokers=True, codes=False, return_not_print=False):
        self.jokers = jokers
        self.codes = codes
        self.return_not_print = return_not_print

        # Build full deck
        self.deck_full = [s + str(n) for s in ["c", "h", "d", "s"] for n in list(range(10)) + ["j", "q", "k"]]
        if self.jokers:
            self.deck_full += ["jo", "jo"]

        # Start with a fresh, unshuffled deck
        self.deck_current = self.deck_full.copy()
        self.deck_dealt = []

    def identify_card(self, card): # Turn a 2-character code into a full name, e.g. 'c5' -> '5 of Clubs'
        if card == "jo": # Case: Joker
            return "Joker"

        if len(card) != 2: # Case: Not a valid input
            return None
    
        rank = card[1].lower()

        if rank in [str(n) for n in range(2, 10)]:
            full = rank + " of "
        elif rank == "0":
            full = "10 of "
        elif rank == "1":
            full = "Ace of "
        elif rank == "j":
            full = "Jack of "
        elif rank == "q":
            full = "Queen of "
        elif rank == "k":
            full = "King of "
        else:
            return None

        try:
            full += self.suits.get(card[0].lower(), "")
        except:
            return None
        return full

    def deal(self, cards=1): # Deal a number of cards from the top of the deck
        dealt = []

        for _ in range(cards):
            if len(self.deck_current) == 0:
                print("Out of cards, please reshuffle.")
                dealt.append(None)
                break

            card = self.deck_current.pop()
            self.deck_dealt.append(card)

            if self.codes:
                output = card
            else:
                output = self.identify_card(card)

            if self.return_not_print:
                dealt.append(output)
            else:
                print(output)

        if self.return_not_print:
            return dealt

    def shuffle(self, undealt_only=False): #Shuffle the deck. If undealt_only=False, reshuffle the full deck
        if not undealt_only:
            self.deck_current = self.deck_full.copy()
            self.deck_dealt.clear()

        random.shuffle(self.deck_current)

    def peek(self, cards=1): # Look at the top few cards without removing them
        if cards >= len(self.deck_current):
            cards = len(self.deck_current)

        top_cards = list(reversed(self.deck_current[-cards:]))

        if self.codes:
            output = top_cards
        else:
            output = [self.identify_card(c) for c in top_cards]

        if self.return_not_print:
            return output
        else:
            print(output)

    def remaining(self): # Return the number of undealt cards
        return len(self.deck_current)

    def reset(self): # Reset to a full, unshuffled deck
        self.deck_current = self.deck_full.copy()
        self.deck_dealt.clear()
