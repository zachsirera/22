# This file extends game.py

import helpers

# This is an AI to play the card game 22. This AI adheres to a strict set of rules. Future AI players will invoke more complex decision matrices.

####### Rule outline: #######

## Deal Rules ##

# On initial deal, keep all: 2, 3, Q, K, A
# On initial deal, keep pairs: J
# On initial deal, keep triples: J, 10
# On initial deal, keep quads: J, 10, 9

## Lead Rules ##



## Play Rules ##


cards_list = [
	{"face": "2", "value": 2, "score_value": 2, "deal_2": 5, "deal_3": 5, "deal_4": 5},  
	{"face": "3", "value": 3, "score_value": 3, "deal_2": 5, "deal_3": 5, "deal_4": 5},  
	{"face": "4", "value": 4, "score_value": 4, "deal_2": 5, "deal_3": 5, "deal_4": 5},  
	{"face": "5", "value": 5, "score_value": 5, "deal_2": 5, "deal_3": 5, "deal_4": 5},  
	{"face": "6", "value": 6, "score_value": 6, "deal_2": 6, "deal_3": 6, "deal_4": 6},  
	{"face": "7", "value": 7, "score_value": 7, "deal_2": 7, "deal_3": 7, "deal_4": 7},  
	{"face": "8", "value": 8, "score_value": 8, "deal_2": 8, "deal_3": 8, "deal_4": 7},  
	{"face": "9", "value": 9, "score_value": 9, "deal_2": 9, "deal_3": 9, "deal_4": 7},  
	{"face": "10", "value": 10, "score_value": 10, "deal_2": 10, "deal_3": 10, "deal_4": 7},
	{"face": "J", "value": 11, "score_value": 10, "deal_2": 10, "deal_3": 10, "deal_4": 7}, 
	{"face": "Q", "value": 12, "score_value": 10, "deal_2": 10, "deal_3": 10, "deal_4": 7}, 
	{"face": "K", "value": 13, "score_value": 10, "deal_2": 10, "deal_3": 10, "deal_4": 7},
	{"face": "A", "value": 14, "score_value": 11, "deal_2": 11, "deal_3": 11, "deal_4": 7}]

# This is a variable to test the functions. To be removed.
test_hand = [{"face": "2", "value": 2, "score_value": 2, "deal_2": 5, "deal_3": 5, "deal_4": 5},  
	{"face": "3", "value": 3, "score_value": 3, "deal_2": 5, "deal_3": 5, "deal_4": 5},  
	{"face": "4", "value": 4, "score_value": 4, "deal_2": 5, "deal_3": 5, "deal_4": 5},  
	{"face": "5", "value": 5, "score_value": 5, "deal_2": 5, "deal_3": 5, "deal_4": 5}, 
	{"face": "9", "value": 9, "score_value": 9, "deal_2": 9, "deal_3": 9, "deal_4": 7},
	{"face": "J", "value": 11, "score_value": 10, "deal_2": 10, "deal_3": 10, "deal_4": 7},
	{"face": "J", "value": 11, "score_value": 10, "deal_2": 10, "deal_3": 10, "deal_4": 7},
	{"face": "J", "value": 11, "score_value": 10, "deal_2": 10, "deal_3": 10, "deal_4": 7}]


def toss(hand):
	''' This is a function to apply the rules listed above for the dealback. '''

	# These cards are tossed no matter what
	toss_list = ['4', '5', '6', '7', '8']

	# Create a list that will make it operations easier
	face_list = []
	for card in hand:
		face_list.append(card['face'])

	# Setup the necessary variables for the popping operation
	hand_len = len(face_list)
	rev_hand = reversed(face_list)

	# Pass through and remove the cards that are never kept
	for index, card in enumerate(rev_hand):
		if card in toss_list:
			face_list.pop(hand_len - 1 - index)

	# Pass through and remove cards that are not high value pairs
	if face_list.count('J') > 1:
		pass
	else:
		face_list = [x for x in face_list if x != 'J']

	# Pass through and remove cards that are not high value triplets
	if face_list.count('10') > 2:
		pass 
	else:
		face_list = [x for x in face_list if x != '10']

	# Pass through and remove cards that are not high value quads
	if face_list.count('9') > 3:
		pass 
	else:
		face_list = [x for x in face_list if x != '9']

	# Create and return hand based on remaining items in face_list
	new_hand = []
	for value in face_list:
		card = next((x for x in cards_list if x['face'] == value), None)
		new_hand.append(card)

	helpers.display_hand(new_hand, 1)

	return new_hand




toss(test_hand)