# c=clubs, h=hearts, d=diamonds, s=spades
# j=jack, q=queen, k=king
# 0s are 10s, 1s are aces
# You will need to pre-shuffle before playing

import random

deck_full = [s+str(n) for s in ["c","h","d","s"] for n in list(range(10))+["j","q","k"]]
suits = {"c":"Clubs","h":"Hearts","d":"Diamonds","s":"Spades"}



jokers = True # Change to True in order to play with jokers
codes = False # Change to True in order to only print 2 character codes
return_not_print = False # Change to True in order to have deal function return instead of printing
# i.e., only print "c5" instead of "5 of Clubs"

if jokers:
    deck_full += ["jo","jo"]
    
deck_current = deck_full.copy()
deck_dealt = []

def identify_card(card): # Only used if codes is false, this turns "c5" into "5 of Clubs"
    full = " of "
    if card[1] in [str(n) for n in list(range(2,10))]:
        full = str(card[1]) + full
    elif card[1] == "0":
        full = "10" + full
    elif card[1] == "1":
        full = "Ace" + full
    elif card[1] == "j":
        full = "Jack" + full
    elif card[1] == "q":
        full = "Queen" + full
    else:
        full = "King" + full
    try:
        full += f"{suits[card[0]]}"
    except:
        pass
    if card == "jo":
        full = "Joker"
    return full
    

def deal(cards = 1, deck_current = None, deck_dealt = None): # 2nd and 3rd parameters in order to use own deck
    global codes, return_not_print
    if deck_current == None:
        deck_current = globals()["deck_current"]
    if deck_dealt == None:
        deck_dealt = globals()["deck_dealt"]
    dealt = []
    for i in range(cards):
        if len(deck_current) == 0:
            print("Out of Cards, please reshuffle.")
            dealt.append(None)
            break
        deck_dealt.append(deck_current.pop())
        card = deck_dealt[-1]
        if codes:
            if return_not_print:
                dealt.append(card)
            else:
                print(card)
        else:
            if return_not_print:
                dealt.append(identify_card(card))
            else:
                print(identify_card(card))
    if return_not_print:
        return dealt

def shuffle(undealt_only = False, deck_current = None, deck_dealt = None, deck_full = None): # Shuffle
    
    #Check if we're using our own deck or the user's
    if deck_current == None:
        deck_current = globals()["deck_current"]
    if deck_dealt == None:
        deck_dealt = globals()["deck_dealt"]
    if deck_full == None:
        deck_full = globals()["deck_full"]
        
    if not undealt_only:
        deck_current[:] = deck_full.copy()
        deck_dealt.clear()
    random.shuffle(deck_current)


def peek(cards = 1, deck_current = None): # Look at top cards
    if deck_current == None:
        deck_current = globals()["deck_current"]
    if cards >= len(deck_current):
        cards = len(deck_current)
    if codes:
        if return_not_print:
            # Returns an array, not a string
            return list(reversed(deck_current[-1*cards:]))
        else:
            for c in list(reversed(deck_current[-1*cards:])):
                print(c)
    else:
        #Build list of seen cards
        seen = []
        for i in range(cards):
            seen.append(identify_card(deck_current[-i-1]))
        if return_not_print:
            return seen
        else:
            print(seen)
