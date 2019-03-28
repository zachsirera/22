# This file extends game.py

import helpers

# This is an AI to play the card game 22. This AI is identical in complexity to AI, the only strategic difference is this AI will keep a 4. 

####### Rule outline: #######

## Deal Rules ##

# On initial deal, keep all: 2, 3, 4, Q, K, A
# On initial deal, keep pairs: J
# On initial deal, keep triples: J, 10
# On initial deal, keep quads: J, 10, 9

## Lead Rules ##

# Always lead the lowest single "trash" card in the hand . A trash card is defined as a card not present in the "keep all" list.
# Once all trash cards are removed from the players hand, lead the lowest face value, highest multiple. IE, lead 3 9s before 2 10s.
# Once all multiples have been removed from the players hand, lead the lowest value single that is not a 2 or a 3.
# If the resulting hand from the lead is lower value than A, 2, 3, lead the second lowest single. 

## Play Rules ##

# Always play the lowest value single card that beats the current play on the table.
# Always play the lowest combination of multiples that beats the current play on the table. 
# Split high value pairs rather than playing a higher card. IE, if the hand contains QKKA, play QK instead of QA.
# If multiple low cards and few high cards, play under if the number of cards of the resulting hand minus 1 is greater than the 
# number of high cards. IE, hand: 23KA, Play a 2 to avoid being left in a 23A situation.





# This is a variable to test the functions. To be removed.
test_hand = [{"face": "2", "value": 2, "score_value": 2, "deal_2": 5, "deal_3": 5, "deal_4": 5},  
	{"face": "3", "value": 3, "score_value": 3, "deal_2": 5, "deal_3": 5, "deal_4": 5},  
	{"face": "4", "value": 4, "score_value": 4, "deal_2": 5, "deal_3": 5, "deal_4": 5},  
	{"face": "5", "value": 5, "score_value": 5, "deal_2": 5, "deal_3": 5, "deal_4": 5}, 
	{"face": "9", "value": 9, "score_value": 9, "deal_2": 9, "deal_3": 9, "deal_4": 7},
	{"face": "10", "value": 10, "score_value": 10, "deal_2": 10, "deal_3": 10, "deal_4": 7},
	{"face": "10", "value": 10, "score_value": 10, "deal_2": 10, "deal_3": 10, "deal_4": 7},
	{"face": "10", "value": 10, "score_value": 10, "deal_2": 10, "deal_3": 10, "deal_4": 7},
	{"face": "J", "value": 11, "score_value": 10, "deal_2": 10, "deal_3": 10, "deal_4": 7}]



####### Gameplay functions: #######

def toss(hand):
	''' This is a function to apply the rules listed above for the initial deal. '''
	pass


def lead(hand):
	''' This is a function to apply the rules listed above for the lead '''
	pass


def play(hand):
	''' This is a function to apply the rules listed above for playing in response to the current play '''
	pass








